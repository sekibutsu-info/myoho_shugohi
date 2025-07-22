import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSV読み込み
df = pd.read_csv('妙法守護碑.csv')

# グラフ描画
plt.figure(figsize=(10,6))
plt.ylabel('造立数')
plt.xlabel('造立年')
plt.tight_layout()

# 画像保存
plt.savefig('graph.png')
