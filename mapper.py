#!/usr/local/bin/python
# coding: utf-8
 
import sys, json, codecs
dic = json.load(codecs.open('dic.json', 'r', 'utf-8'))
 
# input comes from STDIN (standard input)
for line in sys.stdin:
    # 行を単語に分割する
    words = line.strip().split()
    for word in words:
        # STDOUT (標準出力)に結果を書き込む;
        # ここで出力したものはReduce(つまりrecuder.py)での入力になる
        # タブ文字での分割; 単語の出現回数は 1
        if word in dic:
            print '%s\t%s' % (word, '1')
