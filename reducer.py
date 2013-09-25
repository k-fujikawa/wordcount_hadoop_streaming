#!/usr/bin/python
# coding: utf-8
from operator import itemgetter
import sys
 
# 単語の出現回数のマップ
word2count = {}
 
# 入力はSTDIN
for line in sys.stdin:
    # 行頭と行末の空白文字を除去
    line = line.strip()
 
    # mapper.pyの出力をパースする
    word, count = line.split('\t', 1)
    # 回数を文字列から数字に変換
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        # 回数が数字でなければ
        # こっそり、この行はなかったことにして捨て去る
        pass
 
# 単語をアスキーソートする
#
# この処理は必要ないが、オフィシャルHadoopの単語の
# カウントサンプルコードの最終出力に似せるために行う。
sorted_word2count = sorted(word2count.items(), key=itemgetter(0))
 
# STDOUT (標準出力)に結果を書き込む
for word, count in sorted_word2count:
    print '%s\t%s'% (word, count)
