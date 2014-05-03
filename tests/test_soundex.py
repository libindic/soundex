# -*- coding: utf-8 -*-

from soundex import getInstance

s = getInstance()


def test_soundex():
    '''TEST: Soundex calculation'''
    assert s.soundex('vasudev') == 'v231'
    assert s.soundex('Rupert') == 'R163'
    assert s.soundex(u'ಬೆಂಗಳೂರು') == u'ಬDNFQCPC'
    assert s.soundex(u'आम्र् फल्') == u'आNPMQ000'


def test_compare():
    '''TEST: Soundex Comparison'''
    assert s.compare('Bangalore', u'ಬೆಂಗಳೂರು') == -1
    assert s.compare(u'ಬೆಂಗಳೂರು', u'बॆंगळूरु') == 1
    assert s.compare(u'बॆंगळूरु', u'बॆंगळूरु') == 0
    assert s.compare(u'बॆंगळूरु', u'आम्र् फल्') == -1
