#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2012-8-25

@author: tanbro
'''

import codecs
import json

def main():
    hanzi_pinyin_tab = {}
    baselatin_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encoding = 'utf-16'
    f = codecs.open(filename='../res/utf_16-pinyin.txt', encoding=encoding)
    for line in f:
        if line[1] in baselatin_lower:
            hanzi_part = line[0]
            pinyin_part = line[1:].strip().split(' ')
            lst = hanzi_pinyin_tab[hanzi_part] = hanzi_pinyin_tab.get(hanzi_part, [])
            for pinyin in pinyin_part:
                if pinyin not in lst:
                    lst.append(pinyin)
            

    hanzi_pinyin_tab_str = json.dumps(hanzi_pinyin_tab)
    f = open('./hanzi2pinyin.json', 'w')
    f.write(hanzi_pinyin_tab_str)
    

        

if __name__ == '__main__':
    main()
