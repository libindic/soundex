# -*- coding: utf-8 -*-

import unittest
from soundex import getInstance


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
        self.assertEqual(self.s.compare(u'ಬೆಂಗಳೂರು', u'बॆंगळूरु'), 1)
        self.assertEqual(self.s.compare(u'बॆंगळूरु', u'बॆंगळूरु'), 0)
        self.assertEqual(self.s.compare(u'बॆंगळूरु', u'आम्र् फल्'), 2)
