#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    translator
    ~~~~~~~~~~

    A translator for command line based on api.fanyi.baidu.com. It't simple and
    convenient.

    :copyright: (c) 2017 by Jason Wang.
    :license: MIT, see LICENSE for more details.
"""
import argparse
import hashlib
import random
import requests

from urllib.parse import quote as url_quote

from . import __version__


from_lang = 'auto'


def get_baidu_url(args):
    """Gen url for baidu_engine"""
    to_lang = args['lang']
    appid = '20151113000005349'
    baidu_api = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    q_word = " ".join(args['word'])
    salt = random.randint(32768, 65536)
    secret_key = 'osubCEzlGjzvw8qdQc41'
    sign = (appid + q_word + str(salt) + secret_key).encode('utf-8')
    mstring = hashlib.md5()
    mstring.update(sign)
    sign = mstring.hexdigest()
    trans_url = baidu_api + '?appid=' + appid + '&q=' + url_quote(q_word) \
                          + '&from='  + from_lang \
                          + '&to='    + to_lang \
                          + '&salt='  + str(salt) + '&sign=' + sign
    return trans_url


def baidu_engine(args):
    """The engine for baidu translator comes from `api.fanyi.baidu.com`"""
    try:
        response = requests.get(get_baidu_url(args), timeout=1)
        return response.json()
    except ConnectionError as ErrConnect:
        print(ErrConnect)
    except TimeoutError as ErrTimeout:
        print(ErrTimeout)


def get_result(args):
    """This function choose different engine by user's option.
    It only supports baidu translator now.
    """
    if args['baidu']:
        return baidu_engine(args)


def get_translation(args):
    """Get the json data from get_result and return translation.
    You can call it when you want format output by yourself.
    """
    translated = get_result(args)
    src = translated['trans_result'][0]['src']
    dst = translated['trans_result'][0]['dst']
    return src, dst


def format_display(args):
    """Format translation.  You can format it by your function."""
    s, d = get_translation(args)
    return "==> " + d


def translate(args):
    """Simple return the tranlation to caller"""
    try:
        return format_display(args) or "Sorry, couldn't translate\n"
    except:
        return 'Failed to establish network connection'


def get_parser():
    """Parse cli arguments"""
    #: Use argparse module is simple when developing a CLA.
    #: prog argument hold the name of this app.
    #: description describes this app.
    prog = 'translate'
    description = 'a translator for command line'
    parser = argparse.ArgumentParser(prog=prog, description=description)
    #: the add_argument() method is used to populate
    #: the parser with actions for optional and positional arguments.
    parser.add_argument('word', metavar='WORD', type=str, nargs='*',
                        help='the word or sentence to be translated'
                        )
    parser.add_argument('-b', '--baidu', action='store_true', default=True,
                        help='use baidu api (default)'
                        )
    parser.add_argument('-t', '--to', action='store', default='zh', dest='lang',
                        help='choose which language to be translated to. '
                        'default is chinese (zh, en, yue, wyw, etc.)'
                        )
#    parser.add_argument('-y', '--youdao', action='store_true',
#                        help='use youdao translator'
#                        )
#    parser.add_argument('-g', '--google', action='store_true',
#                        help='use google translator'
#                        )
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s ' + __version__
                        )
    #: Finally, use parse_args() method to invoke to convert the args at the
    #: command-line into an object with attributes.
    return parser


def main():
    """The entry function"""
    parser = get_parser()
    #: Use vars() to switch object to dict.
    #: So srgs is a dict returned by vars likes
    #: {'version': 'v0.0.1', 'baidu': True, ...}
    #: Next, we can look up values with []
    args = vars(parser.parse_args())

    #: Use this tool is translating,
    #: so a word or sentence should be given.
    if not args['word']:
        parser.print_help()
        return

    #: Simply, print the translated result
    #: to command line is a good choice.
    print(translate(args))


if __name__ == '__main__':
    main()
