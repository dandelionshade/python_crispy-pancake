import pandas as pd

# 读取 CSV 文件
df = pd.read_csv("/workspaces/codespaces-flask/utils/timeline_data_copy.csv")

# 删除 URL 列中的内容
df['URL'] = ""  # 将 URL 列的所有内容设置为空字符串

# 保存修改后的 CSV 文件
df.to_csv("timeline_data_no_url.csv", index=False)

print("URL 链接已删除，修改后的文件保存为 'timeline_data_no_url.csv'")
