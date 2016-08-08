# -*- coding: utf-8 -*-

import unittest
from soundex import getInstance
from soundex import soundex_compare, soundex_soundex


class SoundexTest(unittest.TestCase):
    def setUp(self):
        self.s = getInstance()

    def test_soundex(self):
        '''TEST: Soundex calculation'''
        self.assertEqual(self.s.soundex('vasudev'), 'v231')
        self.assertEqual(self.s.soundex('Rupert'), 'R163')
        self.assertEqual(self.s.soundex(u'ಬೆಂಗಳೂರು'), u'ಬDNFQCPC')
        self.assertEqual(self.s.soundex(u'आम्र् फल्'), u'आNPMQ000')

    def test_compare(self):
        '''TEST: Soundex Comparison'''
        self.assertEqual(self.s.compare('Bangalore', u'ಬೆಂಗಳೂರು'), -1)
        self.assertEqual(self.s.compare(u'ಬೆಂಗಳೂರು', u'बॆंगळूरु'), 2)
        self.assertEqual(self.s.compare(u'बॆंगळूरु', u'बॆंगळूरु'), 0)
        self.assertEqual(self.s.compare(u'बॆंगळूरु', u'आम्र् फल्'), -1)

    def test_soundex_soundex(self):
        '''TEST: Soundex calculation'''
        self.assertEqual(soundex_soundex('vasudev'), 'v231')
        self.assertEqual(soundex_soundex('Rupert'), 'R163')
        self.assertEqual(soundex_soundex(u'ಬೆಂಗಳೂರು'), u'ಬDNFQCPC')
        self.assertEqual(soundex_soundex(u'आम्र् फल्'), u'आNPMQ000')

    def test_soundex_compare(self):
        '''TEST: Soundex Comparison'''
        self.assertEqual(soundex_compare('Bangalore', u'ಬೆಂಗಳೂರು'), -1)
        self.assertEqual(soundex_compare(u'ಬೆಂಗಳೂರು', u'बॆंगळूरु'), 2)
        self.assertEqual(soundex_compare(u'बॆंगळूरु', u'बॆंगळूरु'), 0)
        self.assertEqual(self.s.compare(u'बॆंगळूरु', u'आम्र् फल्'), -1)
