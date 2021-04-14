from 1_5 import 

file_name = "../tw_strings.txt"
f = open(file_name, "r")
tw_strings = f.read().split(',')
f.close()

print(f'----問六----')
# 与えられた文字列のbi-gramをタプルの組みにし、リストに格納する関数、ただし " は含まないものとする
def bigram(s):
  return [(s[i], s[i+1]) for i in range(0, len(s)-1) if s[i] != '"' and s[i+1] != '"']
print(bigram(tw_strings[0]))

print(f'----問七----')
# 与えられた文字列のn-gramをタプルの組みにし、リストに格納する関数
def ngram(n, s):
  ngram = []
  for i in range(len(s) - (n - 1)):
    tpl = tuple()
    for j in range(n):
      tpl += (s[i+j],)
    ngram.append(tpl)
  return ngram
s = "新型コロナのワクチンが欲しい"
print(ngram(3, s))

print(f'----問八----')
# tw_stringsを改行でわけ、#、URL及び不要単語を取り除き、5-gramの出現頻度を数える
def devide_by_ret(s):
  sw = s.split('\n')
  devided_tws = [swt for swt in sw if swt != '']

hash_list = 

for 