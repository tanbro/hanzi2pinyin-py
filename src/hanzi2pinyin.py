#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2012-8-26

@author: tanbro
'''

import os
import json

_map = json.loads(open(os.path.join(os.path.dirname(__file__), ('%s.json') % (os.path.splitext(os.path.basename(__file__))[0]))).read())

STYLE_CAMEL = 1
STYLE_LOWER = 2
STYLE_UPPER = 3

def translate(hanzi, style=STYLE_LOWER, delimiter=' ', encoding='utf-8', firstletter_only=False):
    if isinstance(hanzi, bytes):
        hanzi = hanzi.decode(encoding)
    elif isinstance(hanzi, unicode):
        hanzi = hanzi
    else:
        raise TypeError('parameter hanzi is not str or unicode')
    result = ''
    for hz_char in hanzi:
        if result:
            result += delimiter
        pinyin = _map[hz_char][0]
        if style == STYLE_UPPER:
            pinyin = pinyin.upper()
        elif style == STYLE_CAMEL:
            pinyin = pinyin[0].upper() + pinyin[1:]
        if firstletter_only:
            pinyin = pinyin[0]
        result += pinyin
    return result
            

if __name__ == '__main__':
    
    pass
