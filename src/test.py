#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2012-8-26

@author: tanbro
'''

import unittest

import hanzi2pinyin

class TestTrans(unittest.TestCase):
    def test_simple(self):
        s = hanzi2pinyin.translate('要转换的汉字', style=hanzi2pinyin.STYLE_CAMEL, delimiter='', firstletter_only=True)
        self.assertEqual(s, 'YZHDHZ')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

