from n_1_5 import get_urls, get_hash_tag

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
def devide_by_tw(s):
  sw = s.split('\n')
  devided_tws = [swt for swt in sw if swt != '']
  return devided_tws

def exclude(s, rm_list):
  for rms in rm_list:
    s = s.replace(rms, '')
  return s

hash_list = get_hash_tag(tw_strings)
ng_keys = ['\n','.','=',' ','　','#','(',')','-','/',':','？','、','。','！','「','」','_']
ng_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '０', '１', '２', '３', '４', '５', '６', '７', '８', '９' ]
ng_lowalp = ['a', 'b', 'c' ,'d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ng_upalp = ['A', 'B', 'C' ,'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

devided_tws = []
url_list = []
for tw in tw_strings:
  url_list += get_urls(tw)
  devided_tws.append(''.join(devide_by_tw(tw)))
pgrams = []
# devided_str = ''.join(devided_tws)
for tw in devided_tws:
  elem = exclude(tw, hash_list)
  elem = exclude(elem, url_list)
  elem = exclude(elem, ng_keys)
  elem = exclude(elem, ng_lowalp)
  elem = exclude(elem, ng_upalp)
  elem = exclude(elem, ng_num)
  pgrams += ngram(5, elem)

result = {}
for elem in pgrams:
  if elem not in result:
    result[elem] = 1
  else:
    result[elem] += 1
print(sorted(result.items(), key=lambda x: -x[1])[:10])

print(f'----問九----')
string_1 = '駆け出しエンジニアと繋がりたい'
string_2 = 'フルスタックエンジニアと繋がりたい'
s1 = set(ngram(5, string_1))
s2 = set(ngram(5, string_2))
print(f'{s1}, {s2}')
print(s1 | s2) # 和集合
print(s1 & s2) # 積集合
print(s1 - s2) # 差集合
print(ngram(5, 'エンジニア')[0] in s1)
print(ngram(5, 'エンジニア')[0] in s2)