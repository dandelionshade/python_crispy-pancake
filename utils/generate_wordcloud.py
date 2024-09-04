# import pandas as pd
# from wordcloud import WordCloud
# import plotly.express as px
# import plotly.io as pio
# from io import StringIO

# # 读取数据
# df = pd.read_csv("timeline_data_no_url.csv")

# # 合并标题文本
# text = " ".join(df['Title'])

# # 生成词云
# wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# # 将词云图保存到文件
# wordcloud.to_file('wordcloud_image.png')

# # 使用 Plotly 显示图像
# import matplotlib.image as mpimg
# img = mpimg.imread('wordcloud_image.png')

# fig = px.imshow(img, title="词云图")

# # 将 Plotly 图表保存为 HTML
# html_str = pio.to_html(fig, full_html=False)

# # 将 HTML 保存到文件中（如果需要）
# with open('templates/wordcloud.html', 'w') as f:
#     f.write(html_str)

# # 返回 HTML 字符串
# print(html_str)  # 可用于调试
