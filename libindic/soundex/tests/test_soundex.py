#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Soundex


class SoundexTest(TestCase):
    def setUp(self):
        super(SoundexTest, self).setUp()
        self.instance = Soundex()

    def test_soundex(self):
        '''TEST: Soundex calculation'''
        self.assertEqual(self.instance.soundex('vasudev'), 'v231')
        self.assertEqual(self.instance.soundex('Rupert'), 'R163')
        self.assertEqual(self.instance.soundex(u'ಬೆಂಗಳೂರು'), u'ಬDNFQCPC')
        self.assertEqual(self.instance.soundex(u'आम्र् फल्'), u'आNPMQ000')

    def test_compare(self):
        '''TEST: Soundex Comparison'''
        self.assertEqual(self.instance.compare('Bangalore', u'ಬೆಂಗಳೂರು'), -1)
        self.assertEqual(self.instance.compare(u'ಬೆಂಗಳೂರು', u'बॆंगळूरु'), 1)
        self.assertEqual(self.instance.compare(u'बॆंगळूरु', u'बॆंगळूरु'), 0)
        self.assertEqual(self.instance.compare(u'बॆंगळूरु', u'आम्र् फल्'), 2)
