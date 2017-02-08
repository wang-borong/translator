# -*- coding: utf-8 -*-
"""Test for translate
It's a simple test sample and written in live.
"""
import translator

import unittest


class TranslatorTestCase(unittest.TestCase):
    """Basic test cases."""

    def call_translator(self, words):
        parser = translator.get_parser()
        args = vars(parser.parse_args(words.split(' ')))
        return translator.translate(args)

    def setUp(self):
        self.words_en = ['apple',
                         'happy',
                         'nice to meet you!'
                         ]
        self.words_zh = ['苹果',
                         '你好吗？'
                         ]

    def tearDown(self):
        pass

    def test_translation_to_zh(self):
        words_to_zh = ['==> 苹果',
                       '==> 幸福的',
                       '==> 很高兴认识你!'
                       ]
        for i in range(len(self.words_en)):
            self.assertEqual(self.call_translator(self.words_en[i]), words_to_zh[i])

    def test_translation_to_en(self):
        words_to_en = ['==> Apple',
                       '==> How are you?'
                       ]
        for j in range(len(self.words_zh)):
            self.assertEqual(self.call_translator('-t en ' + self.words_zh[j]), words_to_en[j])


if __name__ == '__main__':
    unittest.main()
