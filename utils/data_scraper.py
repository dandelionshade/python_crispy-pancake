import pandas as pd
from bs4 import BeautifulSoup

# 示例 HTML 数据
html_data = '''
<ul>
    <li>
        2024年8月22日 (星期四)：​<a href="/wiki/%E4%BF%84%E7%83%8F%E6%88%B0%E7%88%AD%E7%83%8F%E8%BB%8D%E9%87%8D%E5%A4%A7%E9%80%B2%E5%B1%95_%E6%94%BB%E5%85%A5%E4%BF%84%E6%9C%AC%E5%9C%9F%E3%80%8C%E8%A7%A3%E6%94%BE%E3%80%8D%E8%98%87%E8%B3%88" title="俄乌战争乌军重大进展 攻入俄本土“解放”苏贾">俄乌战争乌军重大进展 攻入俄本土“解放”苏贾</a>
    </li>
    <li>
        2024年6月22日 (星期六)：​<a href="/wiki/KGB%E8%88%87FSB%E5%B0%8D%E6%8A%97%E8%A5%BF%E8%A5%BF%E4%BC%AF%E5%88%A9%E4%BA%9E%E9%96%93%E8%AB%9C%E8%88%87%E6%81%90%E6%80%96%E5%88%86%E5%AD%90%EF%BC%9AFSB%E8%80%81%E5%B0%87%E5%B0%88%E8%A8%AA" title="KGB与FSB对抗西西伯利亚间谍与恐怖分子：FSB老将专访">KGB与FSB对抗西西伯利亚间谍与恐怖分子：FSB老将专访</a>
    </li>
    <li>
        2024年5月24日 (星期五)：​<a href="/wiki/%E9%A6%99%E6%B8%AF%E7%A7%BB%E6%B0%91%E6%BD%AE%EF%BC%9A%E8%8B%B1%E6%89%B9BNO%E7%B0%BD%E8%AD%89%E9%A6%96%E5%AD%A3%E8%B6%85%E7%83%8F%E5%85%8B%E8%98%AD%E9%9B%A3%E6%B0%91" title="香港移民潮：英批BNO签证首季超乌克兰难民">香港移民潮：英批BNO签证首季超乌克兰难民</a>
    </li>
    <li>
        2024年5月19日 (星期日)：​<a href="/wiki/AI%E7%9B%9C%E7%94%A8%E7%83%8F%E5%A5%B3YouTuber%E8%82%96%E5%83%8F%E6%8D%8F%E9%80%A0%E8%A6%AA%E4%BF%84%E8%A8%80%E8%AB%96" title="AI盗用乌女YouTuber肖像捏造亲俄言论">AI盗用乌女YouTuber肖像捏造亲俄言论</a>
    </li>
    <li>
        2024年5月15日 (星期三)：​<a href="/wiki/%E4%BF%9D%E9%91%A3%E9%81%AD%E4%BF%84%E6%94%B6%E8%B2%B7%E6%93%AC%E5%88%BA%E6%AE%BA%E7%83%8F%E7%B8%BD%E7%B5%B1_%E5%9C%8B%E6%B0%91%E8%AD%A6%E8%A1%9B%E9%9A%8A%E9%95%B7%E8%A2%AB%E7%82%92" title="保镖遭俄收买拟刺杀乌总统 国民警卫队长被炒">保镖遭俄收买拟刺杀乌总统 国民警卫队长被炒</a>
    </li>
    <li>
        2024年5月15日 (星期三)：​<a href="/wiki/%E4%BF%84%E9%80%9A%E7%B7%9D%E7%83%8F%E5%85%A9%E4%BB%BB%E7%B8%BD%E7%B5%B1" title="俄通缉乌两任总统">俄通缉乌两任总统</a>
    </li>
    <li>
        2024年5月15日 (星期三)：​<a href="/wiki/%E4%BF%84%E5%9C%8B%E9%98%B2%E9%83%A8%E9%95%B7%E8%A2%AB%E8%AA%BF%E8%81%B7" title="俄国防部长被调职">俄国防部长被调职</a>
    </li>
    <li>
        2024年3月25日 (星期一)：​<a href="/wiki/%E4%BF%84%EF%BC%9A%E6%AD%A3%E8%99%95%E6%88%B0%E7%88%AD%E7%8B%80%E6%85%8B" title="俄：正处战争状态">俄：正处战争状态</a>
    </li>
    <li>
        2024年3月23日 (星期六)：​<a href="/wiki/%E4%BF%84%E6%81%90%E8%A5%B2145%E6%AD%BB_11%E4%BA%BA%E8%A2%AB%E6%89%A3_%E7%95%B6%E5%B1%80%E6%93%AC%E6%8B%96%E7%83%8F%E8%90%BD%E6%B0%B4" title="俄恐袭145死 11人被扣 当局拟拖乌落水">俄恐袭145死 11人被扣 当局拟拖乌落水</a>
    </li>
    <li>
        2024年3月11日 (星期一)：​<a href="/wiki/%E6%95%99%E5%AE%97%E7%B1%B2%E7%83%8F%E5%85%8B%E8%98%AD%E8%A6%81%E6%9C%89%E5%8B%87%E6%B0%A3%E3%80%8C%E8%88%89%E7%99%BD%E6%97%97%E3%80%8D%EF%BC%9F" title="教宗吁乌克兰要有勇气“举白旗”？">教宗吁乌克兰要有勇气“举白旗”？</a>
    </li>
    <li>
        2024年3月7日 (星期四)：​<a href="/wiki/AI%E7%9B%9C%E8%87%89%E5%AE%A3%E5%82%B3%E4%BF%84_%E7%83%8F%E7%B6%B2%E7%B4%85%E6%80%92%E6%96%A5" title="AI盗脸宣传俄 乌网红怒斥">AI盗脸宣传俄 乌网红怒斥</a>
    </li>
    <li>
        2024年3月6日 (星期三)：​<a href="/wiki/%E6%BE%A4%E9%80%A3%E6%96%AF%E5%9F%BA%E6%AC%B2%E6%92%A4%E6%8F%9B%E7%83%8F%E6%AD%A6%E8%A3%9D%E9%83%A8%E9%9A%8A%E7%B8%BD%E5%8F%B8%E4%BB%A4%E6%89%8E%E7%9B%A7%E6%97%A5%E5%85%A7%EF%BC%9F" title="泽连斯基欲撤换乌武装部队总司令扎卢日内？">泽连斯基欲撤换乌武装部队总司令扎卢日内？</a>
    </li>
    <li>
        2024年2月5日 (星期一)：​<a href="/wiki/%E4%BF%84%E7%83%8F%E5%B1%80%E5%8B%A2%E8%86%A0%E7%9D%80_%E6%99%AE%E4%BA%AC%E8%B5%B4%E8%81%96%E5%BD%BC%E5%BE%97%E5%A0%A1_%E7%B4%80%E5%BF%B5%E5%88%97%E5%AF%A7%E6%A0%BC%E5%8B%92%E6%88%B0%E5%BD%B9%E5%8B%9D%E5%88%A9" title="俄乌局势胶着 普京赴圣彼得堡 纪念列宁格勒战役胜利">俄乌局势胶着 普京赴圣彼得堡 纪念列宁格勒战役胜利</a>
    </li>
    <li>
        2023年12月25日 (星期一)：​<a href="/wiki/%E6%94%BF%E5%A3%93%E4%B8%8B%E4%BF%84%E7%B6%AD%E5%9F%BA%E7%B5%84%E7%B9%94%E8%A2%AB%E6%8C%87%E3%80%8C%E5%A4%96%E5%9C%8B%E7%89%B9%E5%B7%A5%E3%80%8D%E7%84%A1%E5%A5%88%E6%95%A3%E5%A0%B4" title="政压下俄维基组织被指“外国特工”无奈散场">政压下俄维基组织被指“外国特工”无奈散场</a>
    </li>
    <li>
        2023年8月26日 (星期六)：​<a href="/wiki/%E8%8F%AF%E6%A0%BC%E7%B4%8D%E9%A6%96%E9%A0%98%E6%99%AE%E9%87%8C%E6%88%88%E4%BB%BB%E6%AD%BB%E6%96%BC%E7%A9%BA%E9%9B%A3%E4%B9%8B%E8%AC%8E" title="瓦格纳首领普里戈任死于空难之谜">瓦格纳首领普里戈任死于空难之谜</a>
    </li>
    <li>
        2023年8月23日 (星期三)：​<a href="/wiki/%E8%8F%AF%E6%A0%BC%E7%B4%8D%E9%A6%96%E9%A0%98%E6%99%AE%E9%87%8C%E6%88%88%E4%BB%BB%E6%96%99%E7%A9%BA%E9%9B%A3%E4%BA%A1" title="瓦格纳首领普里戈任料空难亡">瓦格纳首领普里戈任料空难亡</a>
    </li>
    <li>
        2023年7月20日 (星期四)：​<a href="/wiki/%E4%BF%84%E5%86%9B%E4%BD%BF%E7%94%A8%E6%97%A0%E4%BA%BA%E6%9C%BA%E5%8F%8A%E5%AF%BC%E5%BC%B9%E5%8F%91%E5%8A%A8%E8%A2%AD%E5%87%BB_%E4%B8%AD%E5%9B%BD%E9%A9%BB%E6%95%96%E5%BE%B7%E8%90%A8%E6%80%BB%E9%A2%86%E9%A6%86%E9%81%AD%E6%B3%A2%E5%8F%8A" title="俄军使用无人机及导弹发动袭击 中国驻敖德萨总领馆遭波及">俄军使用无人机及导弹发动袭击 中国驻敖德萨总领馆遭波及</a>
    </li>
    <li>
        2023年6月29日 (星期四)：​<a href="/wiki/%E4%BF%84%E7%BE%85%E6%96%AF%E7%99%BC%E7%94%9F%E3%80%8C%E4%B8%80%E6%97%A5%E5%85%B5%E8%AE%8A%E3%80%8D" title="俄罗斯发生“一日兵变”">俄罗斯发生“一日兵变”</a>
    </li>
    <li>
        2023年6月9日 (星期五)：​<a href="/wiki/%E4%B9%8C%E5%85%8B%E5%85%B0%E5%8F%91%E8%B5%B7%E5%8F%8D%E6%94%BB" title="乌克兰发起反攻">乌克兰发起反攻</a>
    </li>
    <li>
        2023年6月7日 (星期三)：​<a href="/wiki/%E5%9F%83%E5%B0%94%E5%A4%9A%E5%AE%89%E5%88%86%E5%88%AB%E4%B8%8E%E4%BF%84%E4%B9%8C%E6%80%BB%E7%BB%9F%E9%80%9A%E7%94%B5%E8%AF%9D_%E5%91%BC%E5%90%81%E6%9F%A5%E6%B8%85%E6%B0%B4%E5%9D%9D%E9%81%AD%E8%A2%AD%E4%BA%8B%E4%BB%B6" title="埃尔多安分别与俄乌总统通电话 呼吁查清水坝遭袭事件">埃尔多安分别与俄乌总统通电话 呼吁查清水坝遭袭事件</a>
    </li>
    <li>
        2023年6月6日 (星期二)：​<a href="/wiki/%E4%B9%8C%E5%85%8B%E5%85%B0%E8%B5%AB%E5%B0%94%E6%9D%BE%E5%9C%B0%E5%8C%BA%E6%B0%B4%E5%9D%9D%E9%81%87%E8%A2%AD_%E5%BD%93%E5%9C%B0%E5%B1%85%E6%B0%91%E7%B4%A7%E6%80%A5%E6%92%A4%E7%A6%BB%E4%B8%AD" title="乌克兰赫尔松地区水坝遇袭 当地居民紧急撤离中">乌克兰赫尔松地区水坝遇袭 当地居民紧急撤离中</a>
    </li>
    <li>
        2023年5月29日 (星期一)：​<a href="/wiki/%E4%BF%84%E7%BE%85%E6%96%AF%E5%B0%8D%E7%BE%8E%E5%9C%8B%E5%8F%83%E8%AD%B0%E5%93%A1%E6%A0%BC%E9%9B%B7%E5%8E%84%E5%A7%86%E7%99%BC%E5%87%BA%E9%80%9A%E7%B7%9D%E4%BB%A4" title="俄罗斯对美国参议员格雷厄姆发出通缉令">俄罗斯对美国参议员格雷厄姆发出通缉令</a>
    </li>
    <li>
        2023年5月27日 (星期六)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E5%A3%B0%E7%A7%B0_%E5%9C%A8%E5%85%8B%E9%87%8C%E7%B1%B3%E4%BA%9A%E4%B8%8A%E7%A9%BA%E5%87%BB%E8%90%BD%E4%B8%A4%E6%9E%9A%E4%B9%8C%E5%85%8B%E5%85%B0%E5%AF%BC%E5%BC%B9" title="俄罗斯声称 在克里米亚上空击落两枚乌克兰导弹">俄罗斯声称 在克里米亚上空击落两枚乌克兰导弹</a>
    </li>
    <li>
        2023年5月24日 (星期三)：​<a href="/wiki/%E8%87%AA%E7%94%B1%E4%BF%84%E7%BD%97%E6%96%AF%E5%86%9B%E5%9B%A2%E8%BF%9B%E6%94%BB%E4%BF%84%E7%BD%97%E6%96%AF%E5%88%AB%E5%B0%94%E5%93%A5%E7%BD%97%E5%BE%B7%E5%9C%B0%E5%8C%BA" title="自由俄罗斯军团进攻俄罗斯别尔哥罗德地区">自由俄罗斯军团进攻俄罗斯别尔哥罗德地区</a>
    </li>
    <li>
        2023年5月21日 (星期日)：​<a href="/wiki/%E6%B3%BD%E8%BF%9E%E6%96%AF%E5%9F%BA%E4%B8%8E%E6%8B%9C%E7%99%BB%E4%BC%9A%E9%9D%A2_%E5%BC%BA%E8%B0%83%E5%B7%B4%E8%B5%AB%E7%A9%86%E7%89%B9%E4%BB%8D%E6%9C%AA%E5%AE%8C%E5%85%A8%E8%A2%AB%E4%BF%84%E5%86%9B%E5%8D%A0%E9%A2%86" title="泽连斯基与拜登会面 强调巴赫穆特仍未完全被俄军占领">泽连斯基与拜登会面 强调巴赫穆特仍未完全被俄军占领</a>
    </li>
    <li>
        2023年5月19日 (星期五)：​<a href="/wiki/G7%E5%B9%BF%E5%B2%9B%E5%B3%B0%E4%BC%9A%E5%BC%80%E5%B9%95%E9%A6%96%E6%97%A5_%E5%85%AC%E5%B8%83%E6%9C%89%E5%85%B3%E4%BF%84%E4%B9%8C%E6%88%98%E4%BA%89%E5%A3%B0%E6%98%8E" title="G7广岛峰会开幕首日 公布有关俄乌战争声明">G7广岛峰会开幕首日 公布有关俄乌战争声明</a>
    </li>
    <li>
        2023年5月19日 (星期五)：​<a href="/wiki/20%E4%B8%87%E4%BF%84%E5%86%9B%E5%9C%A8%E4%B9%8C%E5%85%8B%E5%85%B0%E6%88%98%E5%9C%BA%E4%B8%8A%E9%98%B5%E4%BA%A1" title="20万俄军在乌克兰战场上阵亡">20万俄军在乌克兰战场上阵亡</a>
    </li>
    <li>
        2023年5月14日 (星期日)：​<a href="/wiki/%E4%B9%8C%E5%85%8B%E5%85%B0%E6%80%BB%E7%BB%9F%E6%B3%BD%E4%BC%A6%E6%96%AF%E5%9F%BA%E8%AE%BF%E9%97%AE%E5%BE%B7%E5%9B%BD" title="乌克兰总统泽伦斯基访问德国">乌克兰总统泽伦斯基访问德国</a>
    </li>
    <li>
        2023年5月10日 (星期三)：​<a href="/wiki/%E6%B3%95%E6%96%B0%E7%A4%BE%E8%AE%B0%E8%80%85%E9%98%BF%E5%B0%94%E6%9B%BC%C2%B7%E7%B4%A2%E4%B8%81%E5%9C%A8%E5%B7%B4%E8%B5%AB%E7%A9%86%E7%89%B9%E6%88%98%E5%BD%B9%E4%B8%AD%E6%AE%89%E8%81%8C" title="法新社记者阿尔曼·索丁在巴赫穆特战役中殉职">法新社记者阿尔曼·索丁在巴赫穆特战役中殉职</a>
    </li>
    <li>
        2023年5月7日 (星期日)：​<a href="/wiki/%E7%93%A6%E6%A0%BC%E7%BA%B3%E9%9B%87%E4%BD%A3%E5%85%B5%E9%9B%86%E5%9B%A2%E8%B4%9F%E8%B4%A3%E4%BA%BA%E6%99%AE%E9%87%8C%E6%88%88%E6%B4%A5%E7%A7%B0%E5%B0%86%E6%92%A4%E5%87%BA%E5%B7%B4%E8%B5%AB%E7%A9%86%E7%89%B9" title="瓦格纳雇佣兵集团负责人普里戈津称将撤出巴赫穆特">瓦格纳雇佣兵集团负责人普里戈津称将撤出巴赫穆特</a>
    </li>
    <li>
        2023年5月6日 (星期六)：​<a href="/wiki/%E4%BF%84%E5%A4%96%E4%BA%A4%E9%83%A8%E5%89%AF%E9%83%A8%E9%95%BF%E7%A7%B0%E4%BF%84%E7%BD%97%E6%96%AF%E4%B8%8E%E7%BE%8E%E5%9B%BD%E5%A4%84%E4%BA%8E%E6%88%98%E4%BA%89%E8%BE%B9%E7%BC%98" title="俄外交部副部长称俄罗斯与美国处于战争边缘">俄外交部副部长称俄罗斯与美国处于战争边缘</a>
    </li>
    <li>
        2023年5月5日 (星期五)：​<a href="/wiki/%E4%BF%84%E4%B9%8C%E5%8F%8C%E6%96%B9%E4%BB%A3%E8%A1%A8%E5%9B%A2%E5%9C%A8%E9%BB%91%E6%B5%B7%E7%BB%8F%E6%B5%8E%E5%90%88%E4%BD%9C%E4%BC%9A%E8%AE%AE%E4%B8%8A%E5%8F%91%E7%94%9F%E4%B8%A5%E9%87%8D%E5%86%B2%E7%AA%81" title="俄乌双方代表团在黑海经济合作会议上发生严重冲突">俄乌双方代表团在黑海经济合作会议上发生严重冲突</a>
    </li>
    <li>
        2023年5月5日 (星期五)：​<a href="/wiki/%E6%A2%85%E5%BE%B7%E9%9F%A6%E6%9D%B0%E5%A4%AB%E5%A3%B0%E7%A7%B0%E8%A6%81%E4%BB%8E%E7%89%A9%E7%90%86%E4%B8%8A%E6%B6%88%E7%81%AD%E4%B9%8C%E5%85%8B%E5%85%B0%E6%80%BB%E7%BB%9F%E6%B3%BD%E8%BF%9E%E6%96%AF%E5%9F%BA%E5%8F%8A%E5%85%B6%E9%9B%86%E5%9B%A2" title="梅德韦杰夫声称要从物理上消灭乌克兰总统泽连斯基及其集团">梅德韦杰夫声称要从物理上消灭乌克兰总统泽连斯基及其集团</a>
    </li>
    <li>
        2023年5月3日 (星期三)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E6%8C%87%E6%8E%A7%E6%98%A8%E5%A4%9C%E4%B9%8C%E5%85%8B%E5%85%B0%E8%AF%95%E5%9B%BE%E7%94%A8%E6%97%A0%E4%BA%BA%E6%9C%BA%E8%A2%AD%E5%87%BB%E6%99%AE%E4%BA%AC" title="俄罗斯指控昨夜乌克兰试图用无人机袭击普京">俄罗斯指控昨夜乌克兰试图用无人机袭击普京</a>
    </li>
    <li>
        2023年5月2日 (星期二)：​<a href="/wiki/%E4%BF%84%E4%B9%8C%E6%88%98%E4%BA%89%EF%BC%9A2%E4%B8%87%E4%BF%84%E7%BD%97%E6%96%AF%E5%86%9B%E4%BA%BA%E5%9C%A8%E4%B9%8C%E4%B8%9C%E6%AE%92%E5%91%BD" title="俄乌战争：2万俄罗斯军人在乌东殒命">俄乌战争：2万俄罗斯军人在乌东殒命</a>
    </li>
    <li>
        2023年4月30日 (星期日)：​<a href="/wiki/%E8%81%94%E5%90%88%E5%9B%BD%E5%86%B3%E8%AE%AE%E5%8C%85%E5%90%AB%E2%80%9C%E4%BF%84%E7%BD%97%E6%96%AF%E4%BE%B5%E7%95%A5%E4%B9%8C%E5%85%8B%E5%85%B0%E2%80%9D_%E4%B8%AD%E5%9B%BD%E6%8A%95%E8%B5%9E%E6%88%90%E7%A5%A8" title="联合国决议包含“俄罗斯侵略乌克兰” 中国投赞成票">联合国决议包含“俄罗斯侵略乌克兰” 中国投赞成票</a>
    </li>
    <li>
        2023年4月30日 (星期日)：​<a href="/wiki/%E3%80%8C%E6%88%91%E8%A6%BA%E5%BE%97%E9%80%99%E5%8F%AA%E6%98%AF%E5%80%8B%E5%A4%A2%E3%80%8D%EF%BC%9A%E6%AF%8D%E5%AD%90%E5%BE%9E%E7%83%8F%E5%85%8B%E8%98%AD%E9%80%83%E5%88%B0%E4%BF%84%E7%BE%85%E6%96%AF" title="“我觉得这只是个梦”：母子从乌克兰逃到俄罗斯">“我觉得这只是个梦”：母子从乌克兰逃到俄罗斯</a>
    </li>
    <li>
        2023年4月26日 (星期三)：​<a href="/wiki/%E4%B8%AD%E5%9B%BD%E9%A9%BB%E6%B3%95%E5%A4%A7%E4%BD%BF%E5%8D%A2%E6%B2%99%E9%87%8E%E7%A7%B0%E5%89%8D%E8%8B%8F%E8%81%94%E5%9B%BD%E5%AE%B6%E6%97%A0%E4%B8%BB%E6%9D%83%E5%9C%B0%E4%BD%8D%E6%83%B9%E8%AE%AE" title="中国驻法大使卢沙野称前苏联国家无主权地位惹议">中国驻法大使卢沙野称前苏联国家无主权地位惹议</a>
    </li>
    <li>
        2023年4月18日 (星期二)：​<a href="/wiki/%E6%99%AE%E4%BA%AC%E5%92%8C%E6%B3%BD%E8%BF%9E%E6%96%AF%E5%9F%BA%E7%9A%86%E5%89%8D%E5%BE%80%E6%88%98%E4%BA%89%E5%89%8D%E7%BA%BF%E9%BC%93%E8%88%9E%E5%A3%AB%E6%B0%94" title="普京和泽连斯基皆前往战争前线鼓舞士气">普京和泽连斯基皆前往战争前线鼓舞士气</a>
    </li>
    <li>
        2023年4月16日 (星期日)：​<a href="/wiki/%E4%B9%8C%E5%85%8B%E5%85%B0%E5%B0%86%E4%B8%AD%E5%9B%BD%E5%B0%8F%E7%B1%B3%E5%88%97%E4%B8%BA%E6%88%98%E4%BA%89%E8%B5%9E%E5%8A%A9%E5%95%86" title="乌克兰将中国小米列为战争赞助商">乌克兰将中国小米列为战争赞助商</a>
    </li>
    <li>
        2023年4月14日 (星期五)：​<a href="/wiki/%E7%BE%8E%E5%9C%8B%E6%A9%9F%E5%AF%86%E6%96%87%E4%BB%B6%E5%A4%96%E6%B4%A9_%E7%95%B6%E5%B1%80%E7%9B%B8%E4%BF%A1%E7%96%91%E7%8A%AF%E7%82%BA%E9%BA%BB%E7%9C%81%E5%9C%8B%E6%B0%91%E8%AD%A6%E8%A1%9B%E7%A9%BA%E8%BB%8D" title="美国机密文件外泄 当局相信疑犯为麻省国民警卫空军">美国机密文件外泄 当局相信疑犯为麻省国民警卫空军</a>
    </li>
    <li>
        2023年4月13日 (星期四)：​<a href="/wiki/%E4%BF%84%E4%B9%8C%E6%88%98%E4%BA%89%EF%BC%9A%E4%B9%8C%E5%85%8B%E5%85%B0%E8%A2%AB%E4%BF%98%E5%A3%AB%E5%85%B5%E7%96%91%E9%81%AD%E5%89%B2%E9%A6%96" title="俄乌战争：乌克兰被俘士兵疑遭割首">俄乌战争：乌克兰被俘士兵疑遭割首</a>
    </li>
    <li>
        2023年4月9日 (星期日)：​<a href="/wiki/%E9%A6%AC%E5%85%8B%E9%BE%8D%E4%B8%AD%E5%9C%8B%E8%A1%8C_%E7%B6%93%E8%B2%BF%E6%88%90%E6%9E%9C%E6%98%AD%E7%84%B6%EF%BC%9A%E8%AA%BF%E8%A7%A3%E7%83%8F%E5%85%8B%E8%98%AD%E6%9C%AA%E9%81%82_%E5%8F%B0%E6%B5%B7%E7%AB%8B%E5%A0%B4%E5%8F%97%E8%A9%AC" title="马克龙中国行 经贸成果昭然：调解乌克兰未遂 台海立场受诟">马克龙中国行 经贸成果昭然：调解乌克兰未遂 台海立场受诟</a>
    </li>
    <li>
        2023年4月5日 (星期三)：​<a href="/wiki/%E8%8A%AC%E5%85%B0%E8%AE%AE%E4%BC%9A%E9%80%89%E4%B8%BE%EF%BC%9A%E6%B0%91%E6%97%8F%E8%81%94%E5%90%88%E5%85%9A%E8%8E%B7%E8%83%9C%EF%BC%8C%E5%A5%A5%E5%B0%94%E6%B3%A2%E5%B0%86%E7%BB%84%E5%BB%BA%E6%96%B0%E6%94%BF%E5%BA%9C" title="芬兰议会选举：民族联合党获胜，奥尔波将组建新政府">芬兰议会选举：民族联合党获胜，奥尔波将组建新政府</a>
    </li>
    <li>
        2023年4月5日 (星期三)：​<a href="/wiki/%E5%BE%B7%E5%9B%BD%E5%9B%BD%E9%98%B2%E9%83%A8%E9%83%A8%E9%95%BF%E7%A7%B0%E4%B8%8D%E4%BC%9A%E5%90%91%E4%B9%8C%E5%85%8B%E5%85%B0%E6%8F%90%E4%BE%9B%E6%9B%B4%E5%A4%9A%E8%B1%B9%E5%BC%8F%E5%9D%A6%E5%85%8B" title="德国国防部部长称不会向乌克兰提供更多豹式坦克">德国国防部部长称不会向乌克兰提供更多豹式坦克</a>
    </li>
    <li>
        2023年4月4日 (星期二)：​<a href="/wiki/%E5%8C%97%E7%BA%A6%E5%B7%B2%E5%90%91%E4%B9%8C%E5%85%8B%E5%85%B0%E6%8F%90%E4%BE%9B4875%E4%BA%BF%E4%BA%BA%E6%B0%91%E5%B8%81%E5%86%9B%E4%BA%8B%E6%8F%B4%E5%8A%A9" title="北约已向乌克兰提供4875亿人民币军事援助">北约已向乌克兰提供4875亿人民币军事援助</a>
    </li>
    <li>
        2023年4月3日 (星期一)：​<a href="/wiki/%E8%8A%AC%E5%85%B0%E5%B0%86%E4%BA%8E4%E6%9C%884%E6%97%A5%E6%AD%A3%E5%BC%8F%E5%8A%A0%E5%85%A5%E5%8C%97%E7%BA%A6" title="芬兰将于4月4日正式加入北约">芬兰将于4月4日正式加入北约</a>
    </li>
    <li>
        2023年4月1日 (星期六)：​<a href="/wiki/%E4%BF%84%E7%BE%85%E6%96%AF%E8%81%AF%E9%82%A6%E5%AE%89%E5%85%A8%E5%B1%80%E4%BB%A5%E3%80%8C%E9%96%93%E8%AB%9C%E7%BD%AA%E3%80%8D%E9%80%AE%E6%8D%95%E7%BE%8E%E5%9C%8B%E8%A8%98%E8%80%85" title="俄罗斯联邦安全局以“间谍罪”逮捕美国记者">俄罗斯联邦安全局以“间谍罪”逮捕美国记者</a>
    </li>
    <li>
        2023年3月31日 (星期五)：​<a href="/wiki/%E5%BE%B7%E5%9C%8B%E9%81%8B%E8%BC%B8%E6%A5%AD%E7%95%8C%E7%BD%B7%E5%B7%A5%EF%BC%8C%E9%90%B5%E8%B7%AF%E8%88%AA%E7%A9%BA%E4%BA%A4%E9%80%9A%E5%9A%B4%E9%87%8D%E5%8F%97%E9%98%BB" title="德国运输业界罢工，铁路航空交通严重受阻">德国运输业界罢工，铁路航空交通严重受阻</a>
    </li>
    <li>
        2023年3月31日 (星期五)：​<a href="/wiki/%E8%8A%AC%E5%85%B0%E5%8D%B3%E5%B0%86%E5%8A%A0%E5%85%A5%E5%8C%97%E7%BA%A6" title="芬兰即将加入北约">芬兰即将加入北约</a>
    </li>
    <li>
        2023年3月29日 (星期三)：​<a href="/wiki/%E7%BE%8E%E5%9B%BD%E6%94%AF%E6%8C%81%E8%AE%BE%E7%89%B9%E5%88%AB%E6%B3%95%E5%BA%AD_%E5%AE%A1%E5%88%A4%E4%BF%84%E7%BD%97%E6%96%AF%E4%BE%B5%E4%B9%8C%E7%BD%AA%E8%A1%8C" title="美国支持设特别法庭 审判俄罗斯侵乌罪行">美国支持设特别法庭 审判俄罗斯侵乌罪行</a>
    </li>
    <li>
        2023年3月27日 (星期一)：​<a href="/wiki/%E4%B8%AD%E5%9B%BD%E8%B5%9B%E4%BA%8B%E4%B8%BE%E5%8A%9E%E6%96%B9%E9%98%BB%E6%8C%A0%E4%B9%8C%E5%85%8B%E5%85%B0%E8%BF%90%E5%8A%A8%E5%91%98%E5%B1%95%E7%A4%BA%E6%B5%B7%E6%8A%A5" title="中国赛事举办方阻挠乌克兰运动员展示海报">中国赛事举办方阻挠乌克兰运动员展示海报</a>
    </li>
    <li>
        2023年3月27日 (星期一)：​<a href="/wiki/%E6%B3%BD%E8%BF%9E%E6%96%AF%E5%9F%BA%E5%88%B0%E8%AE%BF%E5%B7%B4%E8%B5%AB%E7%A9%86%E7%89%B9" title="泽连斯基到访巴赫穆特">泽连斯基到访巴赫穆特</a>
    </li>
    <li>
        2023年3月26日 (星期日)：​<a href="/wiki/%E6%99%AE%E4%BA%AC%E5%B0%87%E5%9C%A8%E7%99%BD%E4%BF%84%E7%BE%85%E6%96%AF%E9%83%A8%E7%BD%B2%E6%88%B0%E8%A1%93%E6%A0%B8%E6%AD%A6" title="普京将在白俄罗斯部署战术核武">普京将在白俄罗斯部署战术核武</a>
    </li>
    <li>
        2023年3月26日 (星期日)：​<a href="/wiki/%E4%BF%84%E7%BE%85%E6%96%AF%E5%8F%97%E5%9C%8B%E9%9A%9B%E5%88%B6%E8%A3%81_%E5%AD%B8%E4%B8%AD%E6%96%87%E4%BA%BA%E6%95%B8%E5%A4%A7%E5%A2%9E" title="俄罗斯受国际制裁 学中文人数大增">俄罗斯受国际制裁 学中文人数大增</a>
    </li>
    <li>
        2023年3月24日 (星期五)：​<a href="/wiki/%E4%BF%84%E7%83%8F%E6%88%B0%E7%88%AD%E4%B8%80%E5%B9%B4%E4%BE%86%EF%BC%8C%E6%93%9A%E5%A0%B1%E4%B8%AD%E5%9C%8B%E5%90%91%E4%BF%84%E5%94%AE1200%E8%90%AC%E7%BE%8E%E5%85%83%E7%84%A1%E4%BA%BA%E6%A9%9F" title="俄乌战争一年来，据报中国向俄售1200万美元无人机">俄乌战争一年来，据报中国向俄售1200万美元无人机</a>
    </li>
    <li>
        2023年3月23日 (星期四)：​<a href="/wiki/%E6%A2%85%E5%BE%B7%E7%BE%85%E5%82%91%E5%A4%AB%EF%BC%9A%E6%9C%89%E5%9C%8B%E5%AE%B6%E9%80%AE%E6%8D%95%E6%99%AE%E4%BA%AC%E5%B0%87%E8%A6%96%E5%90%8C%E5%B0%8D%E4%BF%84%E5%AE%A3%E6%88%B0" title="梅德罗杰夫：有国家逮捕普京将视同对俄宣战">梅德罗杰夫：有国家逮捕普京将视同对俄宣战</a>
    </li>
    <li>
        2023年3月21日 (星期二)：​<a href="/wiki/%E4%B8%AD%E4%BF%84%E5%85%83%E9%A6%96%E8%81%AF%E5%90%88%E8%81%B2%E6%98%8E_%E7%BF%92%E8%BF%91%E5%B9%B3%E8%88%87%E6%99%AE%E4%BA%AC%E5%90%8C%E6%84%8F%E3%80%8C%E5%92%8C%E8%AB%87%E8%A7%A3%E6%B1%BA%E7%83%8F%E5%8D%B1%E6%A9%9F%E3%80%8D" title="中俄元首联合声明 习近平与普京同意“和谈解决乌危机”">中俄元首联合声明 习近平与普京同意“和谈解决乌危机”</a>
    </li>
    <li>
        2023年3月21日 (星期二)：​<a href="/wiki/%E6%97%A5%E6%9C%AC%E9%A6%96%E7%9B%B8%E5%B2%B8%E7%94%B0%E6%96%87%E9%9B%84%E7%AA%81%E8%A8%AA%E7%83%8F%E5%85%8B%E8%98%AD%EF%BC%8C%E4%B8%A6%E6%9C%83%E6%99%A4%E7%83%8F%E5%85%8B%E8%98%AD%E7%B8%BD%E7%B5%B1%E6%BE%A4%E5%80%AB%E6%96%AF%E5%9F%BA" title="日本首相岸田文雄突访乌克兰，并会晤乌克兰总统泽连斯基">日本首相岸田文雄突访乌克兰，并会晤乌克兰总统泽连斯基</a>
    </li>
    <li>
        2023年3月20日 (星期一)：​<a href="/wiki/%E4%B9%A0%E8%BF%91%E5%B9%B3%E8%AE%BF%E9%97%AE%E4%BF%84%E7%BD%97%E6%96%AF_%E6%8A%B5%E8%BE%BE%E8%8E%AB%E6%96%AF%E7%A7%91%E4%B8%8E%E6%99%AE%E4%BA%AC%E4%BC%9A%E9%9D%A2" title="习近平访问俄罗斯 抵达莫斯科与普京会面">习近平访问俄罗斯 抵达莫斯科与普京会面</a>
    </li>
    <li>
        2023年3月19日 (星期日)：​<a href="/wiki/%E5%85%8B%E9%87%8C%E7%B1%B3%E4%BA%9A%E5%85%A5%E4%BF%84%E4%B9%9D%E5%91%A8%E5%B9%B4_%E4%BF%84%E7%BD%97%E6%96%AF%E6%80%BB%E7%BB%9F%E6%99%AE%E4%BA%AC%E7%AA%81%E4%BA%B2%E8%87%AA%E5%88%B0%E8%AE%BF" title="克里米亚入俄九周年 俄罗斯总统普京突亲自到访">克里米亚入俄九周年 俄罗斯总统普京突亲自到访</a>
    </li>
    <li>
        2023年3月18日 (星期六)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E4%B8%8E%E4%B9%8C%E5%85%8B%E5%85%B0%E5%9C%A8%E5%B7%B4%E8%B5%AB%E7%A9%86%E7%89%B9%E5%B1%95%E5%BC%80%E8%A1%80%E6%88%98%EF%BC%8C%E5%8F%8C%E6%96%B9%E7%9A%86%E6%8D%9F%E5%A4%B1%E6%83%A8%E9%87%8D" title="俄罗斯与乌克兰在巴赫穆特展开血战，双方皆损失惨重">俄罗斯与乌克兰在巴赫穆特展开血战，双方皆损失惨重</a>
    </li>
    <li>
        2023年3月18日 (星期六)：​<a href="/wiki/%E6%BE%A4%E5%80%AB%E6%96%AF%E5%9F%BA%E6%8C%87%E7%A4%BA%E7%A0%94%E7%A9%B6%E5%B0%87%E4%BF%84%E7%BE%85%E6%96%AF%E6%9B%B4%E5%90%8D%E7%82%BA%E8%8E%AB%E6%96%AF%E7%A7%91%E5%85%AC%E5%9C%8B" title="泽连斯基指示研究将俄罗斯更名为莫斯科公国">泽连斯基指示研究将俄罗斯更名为莫斯科公国</a>
    </li>
    <li>
        2023年3月18日 (星期六)：​<a href="/wiki/%E5%9C%9F%E8%80%B3%E5%85%B6%E5%AE%A3%E5%B8%83%E5%B0%86%E5%90%AF%E5%8A%A8%E6%89%B9%E5%87%86%E8%8A%AC%E5%85%B0%E5%8A%A0%E5%85%A5%E5%8C%97%E7%BA%A6%E7%A8%8B%E5%BA%8F" title="土耳其宣布将启动批准芬兰加入北约程序">土耳其宣布将启动批准芬兰加入北约程序</a>
    </li>
    <li>
        2023年3月17日 (星期五)：​<a href="/wiki/%E5%9B%BD%E9%99%85%E5%88%91%E4%BA%8B%E6%B3%95%E9%99%A2%E5%90%91%E6%99%AE%E4%BA%AC%E5%8F%91%E5%87%BA%E6%8B%98%E6%8D%95%E4%BB%A4_%E6%8C%87%E6%8E%A7%E5%85%B6%E7%8A%AF%E4%B8%8B%E5%A4%9A%E9%A1%B9%E6%88%98%E4%BA%89%E7%BD%AA%E8%A1%8C" title="国际刑事法院向普京发出拘捕令 指控其犯下多项战争罪行">国际刑事法院向普京发出拘捕令 指控其犯下多项战争罪行</a>
    </li>
    <li>
        2023年3月17日 (星期五)：​<a href="/wiki/%E4%B9%A0%E8%BF%91%E5%B9%B3%E5%87%BA%E8%AE%BF%E4%BF%84%E7%BD%97%E6%96%AF_%E5%B0%86%E4%BA%8E%E4%B8%8B%E5%91%A8%E4%B8%80%E5%90%AF%E7%A8%8B" title="习近平出访俄罗斯 将于下周一启程">习近平出访俄罗斯 将于下周一启程</a>
    </li>
    <li>
        2023年3月17日 (星期五)：​<a href="/wiki/%E7%BE%8E%E5%9B%BD%E6%97%A0%E4%BA%BA%E6%9C%BA%E8%A2%AB%E4%BF%84%E7%BD%97%E6%96%AF%E5%87%BB%E8%90%BD_%E4%BF%84%E5%B0%86%E8%AF%95%E5%9B%BE%E6%89%BE%E5%9B%9E%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%AE%8B%E9%AA%B8" title="美国无人机被俄罗斯击落 俄将试图找回无人机残骸">美国无人机被俄罗斯击落 俄将试图找回无人机残骸</a>
    </li>
    <li>
        2023年3月17日 (星期五)：​<a href="/wiki/%E6%B3%A2%E5%85%B0%E5%B0%86%E5%90%91%E4%B9%8C%E5%85%8B%E5%85%B0%E6%8F%90%E4%BE%9B%E5%9B%9B%E6%9E%B6%E6%88%98%E6%9C%BA_%E7%B3%BB%E5%8C%97%E7%BA%A6%E9%A6%96%E5%9B%BD" title="波兰将向乌克兰提供四架战机 系北约首国">波兰将向乌克兰提供四架战机 系北约首国</a>
    </li>
    <li>
        2023年3月15日 (星期三)：​<a href="/wiki/%E7%BE%8E%E5%86%9B%E4%BE%A6%E5%AF%9F%E6%97%A0%E4%BA%BA%E6%9C%BA%E4%B8%8E%E4%BF%84%E5%86%9B%E6%88%98%E6%9C%BA%E7%9B%B8%E6%92%9E_%E5%9D%A0%E6%AF%81%E9%BB%91%E6%B5%B7" title="美军侦察无人机与俄军战机相撞 坠毁黑海">美军侦察无人机与俄军战机相撞 坠毁黑海</a>
    </li>
    <li>
        2023年3月14日 (星期二)：​<a href="/wiki/%E7%BE%8E%E5%9B%BD%E8%BD%B0%E7%82%B8%E6%9C%BA%E6%A8%A1%E6%8B%9F%E6%A0%B8%E6%89%93%E5%87%BB%E5%9C%A3%E5%BD%BC%E5%BE%97%E5%A0%A1" title="美国轰炸机模拟核打击圣彼得堡">美国轰炸机模拟核打击圣彼得堡</a>
    </li>
    <li>
        2023年3月8日 (星期三)：​<a href="/wiki/%E7%9B%96%E6%B4%9B%E6%99%AE%E6%B0%91%E8%B0%83%EF%BC%9A%E7%BE%8E%E5%9B%BD%E4%BA%BA%E5%AF%B9%E4%B8%AD%E5%9B%BD%E5%A5%BD%E6%84%9F%E9%99%8D%E8%87%B3%E6%9C%80%E4%BD%8E" title="盖洛普民调：美国人对中国好感降至最低">盖洛普民调：美国人对中国好感降至最低</a>
    </li>
    <li>
        2023年3月5日 (星期日)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E7%A9%BA%E5%86%9B%E5%86%9B%E5%AE%98%E8%BD%B0%E7%82%B8%E5%93%88%E5%B0%94%E7%A7%91%E5%A4%AB_%E8%A2%AB%E4%B9%8C%E5%85%8B%E5%85%B0%E6%B3%95%E9%99%A2%E5%88%A4%E5%9B%9A12%E5%B9%B4" title="俄罗斯空军军官轰炸哈尔科夫 被乌克兰法院判囚12年">俄罗斯空军军官轰炸哈尔科夫 被乌克兰法院判囚12年</a>
    </li>
    <li>
        2023年2月27日 (星期一)：​<a href="/wiki/%E7%99%BD%E4%BF%84%E7%BD%97%E6%96%AF%E6%80%BB%E7%BB%9F%E5%8D%A2%E5%8D%A1%E7%94%B3%E7%A7%91%E5%8D%B3%E5%B0%86%E8%AE%BF%E5%8D%8E" title="白俄罗斯总统卢卡申科即将访华">白俄罗斯总统卢卡申科即将访华</a>
    </li>
    <li>
        2023年2月27日 (星期一)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E5%85%A5%E4%BE%B5%E4%B9%8C%E5%85%8B%E5%85%B0%E4%B8%80%E5%91%A8%E5%B9%B4%EF%BC%8C%E6%B3%BD%E8%BF%9E%E6%96%AF%E5%9F%BA%E7%A7%B0%E5%9D%9A%E4%BF%A1%E4%B9%8C%E5%85%8B%E5%85%B0%E5%B0%86%E5%8F%96%E8%83%9C" title="俄罗斯入侵乌克兰一周年，泽连斯基称坚信乌克兰将取胜">俄罗斯入侵乌克兰一周年，泽连斯基称坚信乌克兰将取胜</a>
    </li>
    <li>
        2023年2月22日 (星期三)：​<a href="/wiki/%E6%8B%9C%E7%99%BB%E7%AA%81%E8%AE%BF%E5%9F%BA%E8%BE%85%EF%BC%8C%E6%99%AE%E4%BA%AC%E7%A7%B0%E5%8F%AF%E8%83%BD%E6%81%A2%E5%A4%8D%E6%A0%B8%E8%AF%95%E9%AA%8C" title="拜登突访基辅，普京称可能恢复核试验">拜登突访基辅，普京称可能恢复核试验</a>
    </li>
    <li>
        2023年2月21日 (星期二)：​<a href="/wiki/%E6%99%AE%E4%BA%AC%E8%AA%AA%E6%94%BB%E6%89%93%E7%83%8F%E5%85%8B%E8%98%AD%E6%98%AF%E7%82%BA%E3%80%8C%E9%98%BB%E6%AD%A2%E8%A5%BF%E6%96%B9%E7%AD%96%E5%8B%95%E7%9A%84%E6%88%B0%E7%88%AD%E3%80%8D" title="普京说攻打乌克兰是为“阻止西方策动的战争”">普京说攻打乌克兰是为“阻止西方策动的战争”</a>
    </li>
    <li>
        2023年2月16日 (星期四)：​<a href="/wiki/%E5%A4%9A%E5%9B%BD%E5%87%86%E5%A4%87%E5%90%91%E4%B9%8C%E5%85%8B%E5%85%B0%E6%8F%90%E4%BE%9B%E6%88%98%E8%BD%A6%E5%92%8C%E6%AD%A6%E5%99%A8%E6%8F%B4%E5%8A%A9" title="多国准备向乌克兰提供战车和武器援助">多国准备向乌克兰提供战车和武器援助</a>
    </li>
    <li>
        2023年2月11日 (星期六)：​<a href="/wiki/%E6%B5%B7%E5%85%B3%E6%95%B0%E6%8D%AE%E6%98%BE%E7%A4%BA%E4%B8%AD%E5%9B%BD%E5%90%91%E4%BF%84%E7%BD%97%E6%96%AF%E5%87%BA%E5%8F%A3%E5%95%86%E4%B8%9A%E5%86%9B%E7%94%A8%E8%B4%A7%E7%89%A9%EF%BC%8C%E4%BA%A7%E5%93%81%E7%94%A8%E4%BA%8E%E6%94%AF%E6%8C%81%E4%BF%84%E7%BD%97%E6%96%AF%E5%AF%B9%E4%B9%8C%E5%85%8B%E5%85%B0%E6%88%98%E4%BA%89" title="海关数据显示中国向俄罗斯出口商业军用货物，产品用于支持俄罗斯对乌克兰战争">海关数据显示中国向俄罗斯出口商业军用货物，产品用于支持俄罗斯对乌克兰战争</a>
    </li>
    <li>
        2023年2月9日 (星期四)：​<a href="/wiki/%E7%BE%8E%E5%9C%8B%E6%89%B9%E5%87%86%E5%90%91%E6%B3%A2%E8%98%AD%E5%87%BA%E5%94%AE100%E5%84%84%E7%BE%8E%E5%85%83%E6%AD%A6%E5%99%A8" title="美国批准向波兰出售100亿美元武器">美国批准向波兰出售100亿美元武器</a>
    </li>
    <li>
        2023年2月9日 (星期四)：​<a href="/wiki/%E5%85%A9%E6%9E%9A%E4%BF%84%E7%BE%85%E6%96%AF%E5%B0%8E%E5%BD%88%E6%93%8A%E4%B8%AD%E7%83%8F%E5%85%8B%E8%98%AD%E6%9D%B1%E9%83%A8%E5%93%88%E7%88%BE%E7%A7%91%E5%A4%AB" title="两枚俄罗斯导弹击中乌克兰东部哈尔科夫">两枚俄罗斯导弹击中乌克兰东部哈尔科夫</a>
    </li>
    <li>
        2023年2月9日 (星期四)：​<a href="/wiki/%E6%BE%A4%E5%80%AB%E6%96%AF%E5%9F%BA%E8%A8%AA%E5%95%8F%E8%8B%B1%E5%9C%8B%E6%9C%83%E8%A6%8B%E9%A6%96%E7%9B%B8%E8%BE%9B%E5%81%89%E8%AA%A0%E4%B8%A6%E5%9C%A8%E5%9C%8B%E6%9C%83%E7%99%BC%E8%A1%A8%E8%AC%9B%E8%A9%B1" title="泽连斯基访问英国会见首相辛伟诚并在国会发表讲话">泽连斯基访问英国会见首相辛伟诚并在国会发表讲话</a>
    </li>
    <li>
        2023年2月3日 (星期五)：​<a href="/wiki/%E4%BF%84%E7%BE%85%E6%96%AF%E5%8A%A0%E9%80%9F%E5%B7%B4%E8%B5%AB%E7%A9%86%E7%89%B9%E6%94%BB%E5%8B%A2" title="俄罗斯加速巴赫穆特攻势">俄罗斯加速巴赫穆特攻势</a>
    </li>
    <li>
        2023年2月1日 (星期三)：​<a href="/wiki/%E4%B8%8E%E5%8C%97%E7%BA%A6%E5%BC%80%E6%88%98%EF%BC%9F%E4%BF%84%E4%B8%AD%E5%B0%86%E8%AD%A6%E5%91%8A%E5%8C%97%E7%BA%A6" title="与北约开战？俄中将警告北约">与北约开战？俄中将警告北约</a>
    </li>
    <li>
        2023年1月30日 (星期一)：​<a href="/wiki/2022%E5%B9%B4%E6%96%B0%E8%81%9E%E5%A4%A7%E4%BA%8B%E5%9B%9E%E9%A1%A7" title="2022年新闻大事回顾">2022年新闻大事回顾</a>
    </li>
    <li>
        2023年1月24日 (星期二)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E6%AD%A6%E8%A3%85%E5%8A%9B%E9%87%8F%E6%80%BB%E5%8F%82%E8%B0%8B%E9%95%BF%E5%A3%B0%E7%A7%B0%E4%BF%84%E7%BD%97%E6%96%AF%E5%9C%A8%E4%B8%8E%E6%95%B4%E4%B8%AA%E8%A5%BF%E6%96%B9%E4%B8%96%E7%95%8C%E5%AF%B9%E6%8A%97" title="俄罗斯武装力量总参谋长声称俄罗斯在与整个西方世界对抗">俄罗斯武装力量总参谋长声称俄罗斯在与整个西方世界对抗</a>
    </li>
    <li>
        2023年1月23日 (星期一)：​<a href="/wiki/%E8%95%AD%E7%BE%8E%E7%90%B4%E6%8C%87%E5%8F%B0%E7%81%A3%E5%BE%9E%E7%83%8F%E5%85%8B%E8%98%AD%E6%88%B0%E7%88%AD%E4%B8%AD%E5%90%B8%E5%8F%96%E6%95%99%E8%A8%93_%E9%98%B2%E7%AF%84%E5%8C%97%E4%BA%AC%E5%B0%8D%E5%8F%B0%E5%8B%95%E6%AD%A6" title="萧美琴指台湾从乌克兰战争中吸取教训 防范北京对台动武">萧美琴指台湾从乌克兰战争中吸取教训 防范北京对台动武</a>
    </li>
    <li>
        2023年1月18日 (星期三)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E5%B0%86%E6%89%A9%E5%86%9B%E8%87%B3150%E4%B8%87%E4%BA%BA" title="俄罗斯将扩军至150万人">俄罗斯将扩军至150万人</a>
    </li>
    <li>
        2023年1月13日 (星期五)：​<a href="/wiki/%E5%8C%97%E7%BA%A6%E5%9C%A8%E7%BD%97%E9%A9%AC%E5%B0%BC%E4%BA%9A%E9%83%A8%E7%BD%B2AWACS%E4%BE%A6%E5%AF%9F%E6%9C%BA" title="北约在罗马尼亚部署AWACS侦察机">北约在罗马尼亚部署AWACS侦察机</a>
    </li>
    <li>
        2023年1月6日 (星期五)：​<a href="/wiki/%E4%B9%8C%E5%85%8B%E5%85%B0%E6%8B%92%E7%BB%9D%E5%9C%A8%E4%B8%9C%E6%AD%A3%E6%95%99%E5%9C%A3%E8%AF%9E%E8%8A%82%E6%9C%9F%E9%97%B4%E5%81%9C%E7%81%AB" title="乌克兰拒绝在东正教圣诞节期间停火">乌克兰拒绝在东正教圣诞节期间停火</a>
    </li>
    <li>
        2023年1月4日 (星期三)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E5%86%9B%E9%98%9F%E5%B0%86%E5%9C%A8%E4%BF%84%E4%B9%8C%E6%88%98%E5%9C%BA%E4%B8%8A%E4%BD%BF%E7%94%A8%E6%88%98%E7%95%A5%E8%BD%B0%E7%82%B8%E6%9C%BA" title="俄罗斯军队将在俄乌战场上使用战略轰炸机">俄罗斯军队将在俄乌战场上使用战略轰炸机</a>
    </li>
    <li>
        2022年10月8日 (星期六)：​<a href="/wiki/%E5%85%8B%E9%87%8C%E7%B1%B3%E4%BA%9A%E5%A4%A7%E6%A1%A5%E5%8F%91%E7%94%9F%E7%88%86%E7%82%B8" title="克里米亚大桥发生爆炸">克里米亚大桥发生爆炸</a>
    </li>
    <li>
        2022年10月1日 (星期六)：​<a href="/wiki/%E4%B9%8C%E5%85%8B%E5%85%B0%E6%80%BB%E7%BB%9F%E7%94%B3%E8%AF%B7%E9%80%9A%E8%BF%87%E5%BF%AB%E9%80%9F%E9%80%9A%E9%81%93%E5%8A%A0%E5%85%A5%E5%8C%97%E7%BA%A6" title="乌克兰总统申请通过快速通道加入北约">乌克兰总统申请通过快速通道加入北约</a>
    </li>
    <li>
        2022年9月25日 (星期日)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E5%9B%BD%E9%98%B2%E9%83%A8%E9%83%A8%E9%95%BF%E7%A7%B0%E4%BF%84%E5%86%9B%E5%9C%A8%E4%B9%8C%E5%85%8B%E5%85%B0%E9%98%B5%E4%BA%A15937%E4%BA%BA" title="俄罗斯国防部部长称俄军在乌克兰阵亡5937人">俄罗斯国防部部长称俄军在乌克兰阵亡5937人</a>
    </li>
    <li>
        2022年9月22日 (星期四)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E6%80%BB%E7%BB%9F%E6%99%AE%E4%BA%AC%E5%8F%91%E8%A1%A8%E5%85%A8%E5%9B%BD%E7%94%B5%E8%A7%86%E8%B0%88%E8%AF%9D" title="俄罗斯总统普京发表全国电视谈话">俄罗斯总统普京发表全国电视谈话</a>
    </li>
    <li>
        2022年9月22日 (星期四)：​<a href="/wiki/%E4%BF%84%E7%BD%97%E6%96%AF%E6%80%BB%E7%BB%9F%E6%99%AE%E4%BA%AC%E5%AE%A3%E5%B8%83%E8%BF%9B%E8%A1%8C%E9%83%A8%E5%88%86%E5%8A%A8%E5%91%98" title="俄罗斯总统普京宣布进行部分动员">俄罗斯总统普京宣布进行部分动员</a>
    </li>
    <li>
        2022年9月21日 (星期三)：​<a href="/wiki/%E5%85%A8%E9%9D%A2%E5%BC%80%E6%88%98%E7%9A%84%E8%AE%AF%E5%8F%B7%EF%BC%81%E5%8D%A2%E7%94%98%E6%96%AF%E5%85%8B%E5%92%8C%E9%A1%BF%E6%B6%85%E8%8C%A8%E5%85%8B%E5%B0%86%E5%85%A8%E6%B0%91%E5%85%AC%E6%8A%95%E5%8A%A0%E5%85%A5%E4%BF%84%E7%BD%97%E6%96%AF" title="全面开战的讯号！卢甘斯克和顿涅茨克将全民公投加入俄罗斯">全面开战的讯号！卢甘斯克和顿涅茨克将全民公投加入俄罗斯</a>
    </li>
    <li>
        2022年9月12日 (星期一)：​<a href="/wiki/%E4%B9%8C%E5%85%8B%E5%85%B0%E5%A3%B0%E4%B8%9C%E5%87%BB%E8%A5%BF%EF%BC%8C%E4%BF%84%E7%BD%97%E6%96%AF%E5%86%9B%E9%98%9F%E6%92%A4%E5%87%BA%E5%93%88%E5%B0%94%E7%A7%91%E5%A4%AB" title="乌克兰声东击西，俄罗斯军队撤出哈尔科夫">乌克兰声东击西，俄罗斯军队撤出哈尔科夫</a>
    </li>
    <li>
        2022年2月24日 (星期四)：​<a href="/wiki/%E6%99%AE%E4%BA%AC%E6%8E%88%E6%9D%83%E5%B1%95%E5%BC%80%E7%89%B9%E5%88%AB%E5%86%9B%E4%BA%8B%E8%A1%8C%E5%8A%A8_%E4%BF%84%E4%B9%8C%E6%88%98%E4%BA%89%E5%85%A8%E9%9D%A2%E5%BC%80%E6%89%93" title="普京授权展开特别军事行动 俄乌战争全面开打">普京授权展开特别军事行动 俄乌战争全面开打</a>
    </li>
</ul>
'''

# 解析 HTML
soup = BeautifulSoup(html_data, 'html.parser')

# 提取数据
data = []
for li in soup.find_all('li'):
    date = li.get_text(strip=True).split('：')[0]
    title = li.find('a').get_text()
    href = li.find('a')['href']
    data.append([date, title, href])

# 创建 DataFrame
df = pd.DataFrame(data, columns=['Date', 'Title', 'URL'])

# 保存为 CSV 文件
df.to_csv('timeline_data.csv', index=False, encoding='utf-8')

# 保存为 JSON 文件
df.to_json('timeline_data.json', orient='records', force_ascii=False, indent=4)
