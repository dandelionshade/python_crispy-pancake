from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import imageio  # 使用imageio来加载图像
text = """
平安无事
太平无事
平心定气
欣欣向荣
素昧平生
四海承平
待人接物
七满八平
海不扬波
铸甲销戈
繁荣昌盛
情同手足
丰亨豫大
朗朗乾坤
老之将至
同舟共济
河清海晏
刀枪入库
气满志骄
谈噱自若
闻雷失箸
竹报平安
四海升平
虎落平川
燮和天下
四海波静
有说有笑
虐老兽心
歌舞升平
天下太平
太平盛世
终成泡影
百废具兴
不知老之将至
心怡神旷
国富民安
彼倡此和
情恕理遣
倒载干戈
承平盛世
影只形孤
狗吠不惊
国泰民安
心平气和
旷古未闻
政通人和
鸾飞凤舞
化干戈为玉帛
粉饰太平
海晏河清
民安国泰
含哺鼓腹
患难与共
马放南山
风雨同舟
"""
words = ' '.join(jieba.cut(text))
mask_image_url = "R.png"#更改图片
mask_image = imageio.imread(mask_image_url)
font_path = 'C:\WINDOWS\Fonts\SIMSUN.TTC'  # 这里需要一个支持中文的字体文件，宋体
# font_path = 'C:\WINDOWS\Fonts\STLITI.TTF'  # 这里需要一个支持中文的字体文件，华文隶书
wordcloud = WordCloud(font_path=font_path,  # 指定中文字体
                      width=800, height=800,
                      mask=mask_image,  # 这里指定掩模
                      background_color='white',
                      contour_width=10,  # 边缘轮廓宽度
                      contour_color='steelblue',  # 边缘轮廓颜色
                      min_font_size=2).generate(words)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")  # 使用平滑插值
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig('wordcloud222.png', dpi=800, bbox_inches='tight') # 生成图片
plt.show()