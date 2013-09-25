#!/usr/bin/python
# coding: utf-8

import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
    # 行頭と行末の空白を取り除く
    line = line.strip()
    # 行を単語に分割する
    words = line.split()
    # カウンターを上げる
    for word in words:
        # STDOUT (標準出力)に結果を書き込む;
        # ここで出力したものはReduce(つまりrecuder.py)での
        # 入力になる
        #
        # タブ文字での分割; 単語の出現回数は 1
        print '%s\t%s' % (word, 1)# coding: utf-8
