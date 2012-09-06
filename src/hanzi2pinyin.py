#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2012-8-26

@author: tanbro
'''

import os
import types
import json

# Python3 compatibility:  On python2.5, introduce the bytes alias from 2.6
try:
    bytes
except Exception:
    bytes = str

# Load HanZi -> PinYin map file to a dict
_map = json.loads(open(os.path.join(os.path.dirname(__file__), ('%s.json') % (os.path.splitext(os.path.basename(__file__))[0]))).read())

STYLE_CAMEL = 1
STYLE_LOWER = 2
STYLE_UPPER = 3

def translate(hanzi, style=STYLE_LOWER, delimiter=' ', encoding='utf-8', firstletter_only=False):
    if type(hanzi) in types.StringTypes:
        if isinstance(hanzi, bytes):
            hanzi = hanzi.decode(encoding)
    else:
        raise TypeError('parameter hanzi is not str or bytes')
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
