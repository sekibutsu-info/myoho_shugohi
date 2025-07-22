import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSV読み込み
df = pd.read_csv('妙法守護碑.csv')

min_year = int(min(df['造立年']))
max_year = int(max(df['造立年']) + 1)
years = list(range(min_year,max_year))

count_narrow = [0] * len(years)
count_wide = [0] * len(years)
count_undef = [0] * len(years)

for index, row in df.iterrows():
    if not pd.isnull(row['造立年']):
        idx = int(row['造立年']) - min_year
        if row['分類'] == '狭義':
            count_narrow[idx] += 1
        elif row['分類'] == '広義':
            count_wide[idx] += 1
        elif row['分類'] == '保留':
            count_wide[idx] += 1        # 保留も広義に含める
        elif row['分類'] == '未定義':
            count_undef[idx] += 1

# グラフ描画
plt.figure(figsize=(10,6))
plt.bar(years, count_narrow)
plt.bar(years, count_wide, bottom=count_narrow)
offsets = []
y_maxs = []
for x, y, z in zip(count_narrow, count_wide, count_undef):
  offsets.append(x + y)
  y_maxs.append(x + y + z)
plt.bar(years, count_undef, bottom=offsets)
y_max = max(y_maxs) + 1
plt.ylim(0, y_max)
plt.ylabel('造立数')
plt.xlabel('造立年')
plt.legend(['狭義', '広義/保留', '未定義'])
plt.tight_layout()

# 画像保存
plt.savefig('造立年グラフ.png')
