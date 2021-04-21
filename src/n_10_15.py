# unixコマンド
# head -3 'group_pinfo.csv'
# head -3 'group_binfo.csv'
import pandas as pd
import os
db_path = '../db_dir'
df1 = pd.read_csv(os.path.join(db_path, 'group_pinfo.csv'), index_col=0)
df2 = pd.read_csv(os.path.join(db_path, 'group_binfo.csv'), index_col=0)

print(f'----問十----')
print(df1.head(2))
print(df2.head(2))

print(f'----問十一----')
# !tail -n+2 group_pinfo.csv |wc -l
print(len(df1))

print(f'----問十二----')
# !join -j 1 -t 'group_pinfo.csv' 'group_binfo.csv'
df3 = pd.merge(df1, df2, on='ID', how='inner')
df3.to_csv(os.path.join(db_path, 'group_pbinfo.csv'))
print(df3)

print(f'----問十三----')
# !sed 's/,/ /g' 'group_pinfo.csv'
# !cat 'group_pinfo.csv' | tr ',' ' '
df_pb = df3
df_pb.to_csv(os.path.join(db_path, 'group_pinfo_space.csv'), sep=' ')
print(df_pb)

print(f'----問十四----')
# !cat group_pbinfo.csv | cut --
# delim=',' -f2 > coll.txt
# !cat group_pinfo.csv | cut --
# delim=',' -f6 > col2.txt
# !cat coll.txt
# !echo '---'
# !cat col2.txt
df_x = df_pb['名前'].to_csv('col1.txt', index=None)
df_y = df_pb['趣味'].to_csv('col2.txt', index=None)
print(f'{df_pb["名前"]}\n---\n{df_pb["趣味"]}')
