from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import imageio  # 使用imageio来加载图像

text = """
PUA你 CPU你 KTV你 PPT你 UFO你 M3 又幸福了姐 配享太庙 一吃一个不吱声 小孩姐 小孩哥 公主请上车 哈哈哈~惹到我算是提到棉花啦 
冤种 小镇做题家 团长 退！退！退！ 龙行龘龘 前程朤朤 智能+ 快手短视频 脱光 996 碳中和 city不city 健康最贵 生命无价 好家伙 
真有你的 原来如此 大可不必 人间不值得 打工人 干饭人 野性消费 一键三连 后浪 破防了 有内味儿了 绝绝子 硬核 躺平 二次元 真香警告 
U1S1 暴躁老哥 懂王 老父亲 电子竞技没有爱情 为爱发电 一键复制
"""

words = ' '.join(jieba.cut(text))

mask_image_url = "mask.png"
mask_image = imageio.imread(mask_image_url)

font_path = 'C:\WINDOWS\Fonts\SIMSUN.TTC'  # 这里需要一个支持中文的字体文件，宋体
# font_path = 'C:\WINDOWS\Fonts\STLITI.TTF'  # 这里需要一个支持中文的字体文件，华文隶书

wordcloud = WordCloud(font_path=font_path,  # 指定中文字体
                      width=1800, height=1800,
                      mask=mask_image,  # 这里指定掩模
                      background_color='white',
                      contour_width=0,  # 边缘轮廓宽度
                      contour_color='steelblue',  # 边缘轮廓颜色
                      min_font_size=2).generate(words)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")  # 使用平滑插值
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig('wordcloud.png', dpi=800, bbox_inches='tight') # 生成图片

plt.show()
