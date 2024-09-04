import pandas as pd
import plotly.express as px

# 读取 CSV 文件
df = pd.read_csv("timeline_data.csv")


# 按日期排序
df = df.sort_values("Date")

# 创建 Scatter 图表
fig = px.scatter(df, x="Date", y="Title", 
                 title="俄乌战争乌军重大进展时间线")

fig.show()