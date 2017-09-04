# LibIndic Soundex

[![Build Status](https://travis-ci.org/libindic/soundex.svg?branch=master)](https://travis-ci.org/libindic/soundex)
[![Coverage Status](https://coveralls.io/repos/github/libindic/soundex/badge.svg?branch=master)](https://coveralls.io/github/libindic/soundex?branch=master)

Soundex is phonetic algorithm for indexing names by sound as pronounced in
English. LibIndic's soundex module implements Soundex algorithm for Engish as
well as a modified version of soundex algorithm for Indian languages.

Details on how Soundex is implemented can be found at
[Santhosh's blog](http://thottingal.in/blog/2009/07/26/indicsoundex/)

## Installation
1. Clone the repository `git clone https://github.com/libindic/soundex.git`
2. Change to the cloned directory `cd soundex`
3. Run setup.py to create installable source `python setup.py sdist`
3. Install using pip `pip install dist/libindic-soundex*.tar.gz`

## Usage
```
>>> from libindic.soundex import Soundex
>>> instance = Soundex()
>>> instance.soundex(u"കൃത്രിമം")
u'\u0d15PKPBN00'
>>> instance.compare(u"വിദ്യാർഥി", u"വിദ്യാർദി")
1
>>> instance.compare(u"മോര്", u"മുതിര")
2
```
