# 2020/6/20 の神草ツイート５つ


file_name = "../tw_strings.txt"
f = open(file_name, "r")
tw_strings = f.read().split(',')
f.close()

print(f'総合ツイート数:{len(tw_strings)}')

print(f'----問一----')
cnt = 0
for tw in tw_strings:
    if "#プログラミング初心者" in tw:
        cnt += 1
print(cnt)
print(len([tw for tw in tw_strings if '#プログラミング初心者' in tw]))

print(f'----問二----')
print(f'各ツイートの文字数{[len(e) for e in tw_strings]}')

print(f'----問三----')
for e in tw_strings:
    ew = e.split('\n')
    ewf = [ex for ex in ew if ex != '']
    print(f'{len(ewf)}:{ewf[0:5]}')

print(f'----問四----')
def get_hash_tag(tw_strings):
    result_list = []
    for e in tw_strings:
        ew = e.split('\n')
        for ewh in ew:
            ewhf = ewh.split(' ')
            for eh in ewhf:
                ehs = eh.split('　')
                for ehk in ehs:
                    if '#' in ehk:
                        tag = ehk[1:]
                        if not tag in result_list:
                            result_list.append(ehk[1:])
    return set(result_list)
print(get_hash_tag(tw_strings)) 
print(f'----問五----')
def get_urls(strings):
    res_list = []
    e = strings.split('\n')
    for ew in e:
        ewh = ew.split(' ')
        for es in ewh:
            eh = es.split('　')
            for ex in eh:
                eg = ex.split('（')
                for ey in eg:
                    if 'https://' in ey or 'http://' in ey:
                        res_list.append(ey)
    return res_list
for e in tw_strings:
    print(get_urls(e))

