#!/usr/local/bin/python
# coding: utf-8
from operator import itemgetter
import sys
 
# 単語の出現回数のマップ
word2count = {}
 
# 入力はSTDIN
for line in sys.stdin:
    # mapper.pyの出力をパースする
    word, count = line.strip().split('\t')
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        pass
 
# STDOUT (標準出力)に結果を書き込む
for word in word2count:
    print '%s\t%s'% (word, word2count[word])
