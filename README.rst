translator
===========

translator is microtool for python based on api.fanyi.baidu.com. It's simple
and useful. As you see: it's MIT licensed!

Do you want to translate a word or a sentance when you are reading? Before,
You may open your browser or your dict application to search them. But now,
you just need a command to do this:

.. code:: sh

    $ translate apple
    # ==> 苹果

    $ translator --to en 苹果
    # ==> Apple

    $ translator you are so beautiful!
    # ==> 你是如此美丽!

    $ translator --to en 很高兴见到你!
    # ==> Nice to meet you!

Translator support to translate multiple languages, e.g.,
Chinese, English, Russian, French, Korean, etc.
The source language is auto detected, so all you need is
to specify the destination language:

.. code:: sh

    $ translator --to [dst_lang] [WORDs]

All the language options are zh, en, yue, wyw, jp, kor, fra, spa, th,
ara, ru, pt, de, it, el, nl, pl, bul, est, dan, fin, cs, rom, slo, swe,
hu, cht, vie.


Installation
------------

Sorry, you need dump the source codes to install it so far:

.. code:: sh

    $ git clone https://github.com/stuha/translator.git
    $ cd translator && [sudo] python3 setup.py install

Usage
-----

::

    usage: translate [-h] [-b] [-t LANG] [-v] [WORD [WORD ...]]

    a translator for command line

    positional arguments:
      WORD                the word or sentence to be translated

    optional arguments:
      -h, --help          show this help message and exit
      -b, --baidu         use baidu api (default)
      -t LANG, --to LANG  choose which language to be translated to. default is
                          chinese (zh, en, yue, wyw, etc.)
      -v, --version       show program's version number and exit

Author
------

-  Jason Wang (1724555125@qq.com)

Notes
-----

- It just Works with Python3 now

Development
-----------

-  Checkout the repo
-  Follow pep8

Changes
-------
read CHANGELOG
