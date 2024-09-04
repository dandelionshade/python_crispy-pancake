from flask import Flask, render_template

from utils import generate_wordcloud

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
def index():
    # 生成词云图并获取 HTML 内容
    html_str = generate_wordcloud.main()  # 修改 generate_wordcloud 以返回 HTML 字符串
    return render_template('index.html', plot_html=html_str)

if __name__ == '__main__':
    app.run(debug=True)