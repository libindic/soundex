LibIndic Soundex
================

.. image:: https://img.shields.io/pypi/v/libindic-soundex.svg
    :target: https://pypi.python.org/pypi/libindic-soundex
    :alt: PyPI Version

Soundex is phonetic algorithm for indexing names by sound as pronounced in
English. `LibIndic`_'s soundex module implements Soundex algorithm for Engish as
well as a modified version of soundex algorithm for Indian languages.

Details on how Soundex is implemented can be found at
[Santhosh's blog](http://thottingal.in/blog/2009/07/26/indicsoundex/)

Installation
------------
Python 3 is required. Using with `venv`_ is recommended

  .. code-block:: console

    $ pip install libindic-soundex

Usage
-----

  .. code-block:: Python

    from libindic.soundex import Soundex
    instance = Soundex()
    instance.soundex(u"കൃത്രിമം")
    u'\u0d15PKPBN00'
    instance.compare(u"വിദ്യാർഥി", u"വിദ്യാർദി")
    1
    instance.compare(u"മോര്", u"മുതിര")
    -1
    instance.compare(u'ಬೆಂಗಳೂರು', u'बॆंगळूरु')
    2


.. _`LibIndic`: https://libindic.org
.. _`venv`: https://docs.python.org/3/library/venv.html