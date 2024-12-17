import pandas as pd

# (1) 读取 Excel 文件并存入 DataFrame
file_path = r'D:\homework\python程序设计\第13周 数据分析利器之Pandas\第13周 数据分析利器之Pandas\2018世界杯球队数据.xlsx'
df = pd.read_excel(file_path)

# (2) 输出净胜球（进球减去失球）大于0的球队
df['净胜球'] = df['进球'] - df['失球']
print("\n净胜球大于0的球队：")
print(df[df['净胜球'] > 0])

# (3) 输出被罚红牌的球队
print("\n被罚红牌的球队：")
print(df[df['红牌'] > 0])

# (4) 输出进球成功率（进球数/射门数）超过10%的球队及其进球数和射门数
df['射正率'] = df['进球'] / df['射门'] * 100
print("\n进球成功率超过10%的球队及其进球数和射门数：")
print(df[df['射正率'] > 10][['球队', '进球', '射门', '射正率']])

# (5) 输出进球数超过平均数且被罚黄牌少于5张的球队及其进球数和黄牌数
平均进球数 = df['进球'].mean()
print("\n进球数超过平均数且被罚黄牌少于5张的球队及其进球数和黄牌数：")
print(df[(df['进球'] > 平均进球数) & (df['黄牌'] < 5)][['球队', '进球', '黄牌']])

# (6) 按照进球数降序输出所有球队及进球信息
print("\n按照进球数降序输出所有球队及进球信息：")
print(df[['球队', '进球']].sort_values(by='进球', ascending=False))

# (7) 按照所属区进行分组，按升序统计输出每个区的进球数
print("\n按照所属区进行分组，按升序统计输出每个区的进球数：")
print(df.groupby('所属洲')['进球'].sum().sort_values(ascending=True))
