# -*- coding: utf-8 -*-
'''
  soundex
  ~~~~~~~~

  This module implements soundex algorithm components.

  :copyright: (c) 2009-2012 by Santhosh Thottingal
  :copyright: (c) 2012-2014 by SILPA Developers
  :license: LGPL-3.0+, see LICENSE file for more details
'''

_all_ = ["Soundex", "getInstance"]

from itertools import repeat
from silpa_common import servicemethod
from silpa_common.charmap import get_language, charmap

'''
Soundex class provides methods which can be used to perform Soundex phonetic
algorithm on Indian languages as well as English.
'''


_soundex_map = {
    "soundex_en": ["0", "1", "2", "3", "0", "1", "2", "0", "0", "2", "2", "4",
                   "5", "5", "0", "1", "2", "6", "2", "3", "0", "1", "0", "2",
                   "0", "2"],
    "soundex": ['0', 'N', '0', '0', 'A', 'A', 'B', 'B', 'C', 'C', 'P', 'Q',
                '0', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'F', 'F', 'F', 'F',
                'G', 'H', 'H', 'H', 'H', 'G', 'I', 'I', 'I', 'I', 'J', 'K',
                'K', 'K', 'K', 'L', 'L', 'M', 'M', 'M', 'M', 'N', 'O', 'P',
                'P', 'Q', 'Q', 'Q', 'R', 'S', 'S', 'S', 'T', '0', '0', '0',
                '0', 'A', 'B', 'B', 'C', 'C', 'P', 'P', 'E', 'D', 'D', 'D',
                'D', 'E', 'E', 'E', '0', '0', '0', '0', '0', '0', '0', '0',
                '0', '0', 'E', '0', '0', '0', '0', '0', '0', '0', '0', 'P',
                'Q', 'Q', 'Q', '0', '0', '0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                '0', 'J', 'J', 'Q', 'P', 'P', 'F'],
}


class Soundex(object):

    def soundexCode(self, char):
        '''Return the soundex code for given character

           :param char:
               Character whose soundex code is needed
           :return:
               Returns soundex code if character is found in charmap
               else returns 0
        '''
        lang = get_language(char)
        try:
            if lang == "en_US":
                return _soundex_map["soundex_en"][charmap[lang].index(char)]
            else:
                return _soundex_map["soundex"][charmap[lang].index(char)]
        except:
            # Case of exception KeyError because we don't have soundex
            # mapping for the character
            pass

        return 0

    @servicemethod
    def soundex(self, name, length=8):
        '''Calculate soundex of given string

           This function calculates soundex for Indian language string
           as well as English string.

           This function is exposed as service method for JSONRPC in
           SILPA framework.

           :param name: String whose Soundex value to be calculated
           :param length: Length of final Soundex string, if soundex
                          caculated is more than this it will be
                          truncated to length.
           :return: Soundex string of `name'
        '''
        sndx = []
        fc = name[0]

        # translate alpha chars in name to soundex digits
        for c in name[1:].lower():
            d = str(self.soundexCode(c))

            # remove all 0s from the soundex code
            if d == '0':
                continue

            # duplicate consecutive soundex digits are skipped
            if len(sndx) == 0:
                sndx.append(d)
            elif d != sndx[-1]:
                sndx.append(d)

        # append first character to result
        sndx.insert(0, fc)

        if get_language(name[0]) == 'en_US':
            # Don't padd
            return ''.join(sndx)

        if len(sndx) < length:
            sndx.extend(repeat('0', length))
            return ''.join(sndx[:length])

        return ''.join(sndx[:length])

    @servicemethod
    def compare(self, string1, string2):
        '''Compare soundex of given strings

           This function checks if 2 given strings are phonetically
           sounds same by doing soundex code comparison

           :param string1: First string for comparison
           :param string2: Second string for comparison

           :return: Returns 0 if both strings are same, 1 if strings
                    sound phonetically same, 2 if strings are
                    phonetically not same. We can't perform English
                    cross language comparision if English string is
                    passed as one function will return -1.

        '''
        # do a quick check
        if string1 == string2:
            return 0

        string1_lang = get_language(string1[0])
        string2_lang = get_language(string2[0])

        if (string1_lang == 'en_US' and string2_lang != 'en_US') or \
           (string1_lang != 'en_US' and string2_lang == 'en_US'):
            # Can't Soundex compare English and Indic string
            return -1

        soundex1 = self.soundex(string1)
        soundex2 = self.soundex(string2)

        if soundex1[1:] == soundex2[1:]:
            # Strings sound phonetically same
            return 1

        # Strings are not same
        return 2


def getInstance():
    ''' Return Soundex instance

        This function returns instance of Soundex class and is used
        mainly by SILPA framework

        :return: Soundex instance
    '''
    return Soundex()
