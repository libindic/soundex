'''
  soundex.core
  ~~~~~~~~~~~~

  This module implements soundex algorithm components.

  :copyright: (c) 2009-2012 by Santhosh Thottingal
  :license: LGPL-3.0+, see LICENSE file for more details
'''

# -*- coding: utf-8 -*-

from charmap import *

'''

Soundex class provides methods which can be used to perform Soundex phonetic
algorithm on Indian languages as well as English.


'''

_all_ = [ "Soundex", "getInstance" ]
class Soundex:

    def soundexCode(self,char):
        '''Return the soundex code for given character

          Keyword arguments:
            char   -- Character for which soundex whose soundex code should be
                      calculated
            return -- soundex code for given character or 0 on exceptions and
                      if given character is not valid
        '''
        lang= language(char)
        try:
            if lang == "en_US":
                return charmap["soundex_en"][charmap[lang].index(char)]
            else:
                return charmap["soundex"][charmap[lang].index(char)]    
        except:
            '''In case of any exception- Mostly because of character not found in charmap'''
            return 0    
        return 0    
    
    def soundex(self,name, length=8):
        '''Calculate soundex of given string

          Keyword arguments:
          name   -- String whose soundex should be calculated
          length -- Length of the `name` default value is 8
        '''
        sndx =''
        fc = ''
        # translate alpha chars in name to soundex digits
        for c in name.lower():
            if not fc: fc = c   # remember first letter
            d = str(self.soundexCode(c))
            # remove all 0s from the soundex code
            if d== '0' : continue
            # duplicate consecutive soundex digits are skipped
            if not sndx or (d != sndx[-1]):
                sndx += d
            # replace first digit with first alpha character
            sndx = fc + sndx[1:]


        # return soundex code padded to length characters
        return (sndx + (length * '0'))[:length]
    
    def compare(self,string1, string2):
        '''Compare soundex of given strings

          Keyword arguments:
           string1 -- First string
           string2 -- Second string

           return -- 0 if both strings are same 1 if soundex of both strings are same
        '''
        #do a quick check
        if string1 == string2 : #Exact Match
            return 0 
        soundex1=    self.soundex(string1)
        soundex2=    self.soundex(string2)
        if soundex1 == soundex2    : #Both sounds alike
            return 1
        if    language(string1[0]) == "en_US": 
            return -1 #need not check for crosslanguage for English
        #Check whether the first letters are phonetically same from different languages
        if self.soundexCode( string1[0]) == self.soundexCode(string2[0]):
            if soundex1[1:] == soundex2[1:]    : #Both sounds alike
                return 2    #Strings doesnot match
        return -1    
    def get_module_name(self):
        """
          Return module name
        """
        return "Soundex"
    
    def get_info(self):
        """
         Return a description for module
        """
        return     "Soundex Algorithm for Indian Languages and 'sounds like' search across Indian Languages"    
    
def getInstance():
    '''
      This function actually allows binding of soundex module to SILPA framework.
      Provides an instance of Soundex class
    '''
    return Soundex()

            
