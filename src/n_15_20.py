import pandas as pd
import os
db_path = '../db_dir'
df1 = pd.read_csv(os.path.join(db_path, 'group_pinfo.csv'), index_col=0)
df2 = pd.read_csv(os.path.join(db_path, 'group_binfo.csv'), index_col=0)
df_pb = pd.read_csv(os.path.join(db_path, 'group_pbinfo.csv'), index_col=0)

print(f'----問十五----')
df_pb1 = df_pb.iloc[:1, :]
df_pb2 = df_pb.iloc[1:, :]
dfi = pd.DataFrame(
  [
    {
      'ID': 6,
      '名前': 'としお',
      '年齢': 54,
      '性別': '男',
      '担当': 'ボーカル',
      '趣味': 'クッキング'
    }
  ],
  index=[6]
)
df_con = pd.concat([
  df_pb1, dfi, df_pb2 
]).set_index('ID')
print(df_con)

print(f'----問十六----')
n = 2 # int(input())
div_idx = len(df_pb)//n
df_pbi = df_pb
df_pbi.iloc[0:div_idx, :].to_csv(os.path.join(db_path, 'pbi_aa.csv'),index=None)
df_pbi.iloc[div_idx:, :].to_csv(os.path.join(db_path, 'pbi_ab.csv'), header=None)

print(f'----問十七----') # 担当の列のみ
print(df_pb.iloc[:, 4].unique()) # 担当の右の列
print(df_pb.iloc[:, 3].unique())
print(df_pb['担当'].unique())

print(f'----問十八----')# 年齢の大きい順
df = df_pb
df.sort_values('年齢', ascending=False)
print(df.sort_values('年齢', ascending=False))

print(f'----問十九----')# 年齢の大きい順
df_19 = df_pb
print(df_19['担当'].value_counts())

