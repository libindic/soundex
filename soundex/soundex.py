#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2009 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in


import sys
import os
import re
from common import *
class Soundex(SilpaModule):
    def __init__(self):
        self.template=os.path.join(os.path.dirname(__file__), 'soundex.html')
        self.response = SilpaResponse(self.template)
    def soundexCode(self,char):
        index=0
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
    
    @ServiceMethod        
    def soundex(self,name, len=8):
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


        # return soundex code padded to len characters
        return (sndx + (len * '0'))[:len]
    
    @ServiceMethod        
    def compare(self,string1, string2):
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
        return "Soundex"
    def get_info(self):
        return     "Soundex Algorithm for Indian Languages and 'sounds like' search across Indian Languages"    
    
def getInstance():
    return Soundex()

            
