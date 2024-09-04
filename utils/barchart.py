import pandas as pd
import plotly.express as px

# 读取 CSV 文件
df = pd.read_csv("timeline_data.csv")

# 按日期排序
df = df.sort_values("Date")

# 按日期计算事件数量
event_counts = df["Date"].value_counts().sort_index()

# 将数据转化为 DataFrame 以便绘图
event_df = event_counts.reset_index()
event_df.columns = ["Date", "Number of Events"]

# 创建条形图
fig = px.bar(event_df, x="Date", y="Number of Events", 
             title="俄乌战争乌军重大进展时间线",
             labels={"Number of Events": "事件数量", "Date": "日期"},
             text="Number of Events")

# 显示图表
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(xaxis_title="日期", yaxis_title="事件数量", xaxis_tickformat="%Y-%m-%d")
fig.show()
