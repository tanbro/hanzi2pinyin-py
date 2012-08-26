#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Created on 2012-8-26

@author: tanbro
'''

import hanzi2pinyin


if __name__ == '__main__':
    print hanzi2pinyin.translate('王八蛋', style=hanzi2pinyin.STYLE_CAMEL, delimiter='', firstletter_only=True)
    print hanzi2pinyin.translate('大美女')
