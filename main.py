import streamlit as st
import numpy as np
from datetime import date

st.title("🍵和菓子占い！")
"どうぶつ占いの結果をもとに、和菓子をオススメします！"
"powered by 継承工学総合研究所"

birthday = st.date_input(
    "🎉生年月日を選択してください🎉",
    min_value = date(1900, 1, 1),
    max_value = date.today(),
    value=date(1983, 6, 16)
)

gap_days = (birthday - date(1921, 1, 1)).days

animal_list = [
"1.行動力のあるチーター.（イエロー）",
"2.素直なたぬき.（グリーン）",
"3.世話好きな猿.（レッド）",
"4.交流上手な子守熊(コアラ).（オレンジ）",
"5.上昇志向の黒ひょう.（ブラウン）",
"6.度胸のある虎.（ブラック）",
"7.独創性のあるチーター.（ゴールド）",
"8.着実なたぬき.（シルバー）",
"9.努力家の猿.（ブルー）",
"10.駆け引き上手な子守熊(コアラ).（パープル）",
"11.寂しがり屋のこじか.（イエロー）",
"12.完璧主義なゾウ.（グリーン）",
"13.孤高の狼.（レッド）",
"14.好き嫌いのはっきりしたひつじ.（オレンジ）",
"15.器用な猿.（ブラウン）",
"16.世話好きな子守熊(コアラ).（ブラック）",
"17.負けず嫌いなこじか.（ゴールド）",
"18.親分肌のゾウ.（シルバー）",
"19.義理人情に厚い狼.（ブルー）",
"20.安定志向のひつじ.（パープル）",
"21.自由を愛するペガサス.（イエロー）",
"22.天才肌のペガサス.（グリーン）",
"23.無邪気なひつじ.（レッド）",
"24.マイペースな狼.（オレンジ）",
"25.研究熱心な狼.（ブラウン）",
"26.実直なひつじ.（ブラック）",
"27.理想を求めるペガサス.（ゴールド）",
"28.純粋なペガサス.（シルバー）",
"29.謙虚なひつじ.（ブルー）",
"30.発想力に富んだ狼.（パープル）",
"31.誠実なゾウ.（イエロー）",
"32.好奇心旺盛なこじか.（グリーン）",
"33.負けず嫌いな子守熊.(コアラ（レッド）",
"34.順応性の高い猿.（オレンジ）",
"35.用意周到なひつじ.（ブラウン）",
"36.信念を持った狼.（ブラック）",
"37.几帳面なゾウ.（ゴールド）",
"38.好き嫌いの激しいこじか.（シルバー）",
"39.感受性豊かな子守熊(コアラ).（ブルー）",
"40.堅実で真面目な猿.（パープル）",
"41.腰の低いたぬき.（イエロー）",
"42.即断即決のチーター.（グリーン）",
"43.誠実な虎.（レッド）",
"44.流行に敏感な黒ひょう.（オレンジ）",
"45.現実主義な子守熊(コアラ).（ブラウン）",
"46.着実に進む猿.（ブラック）",
"47.人情味あふれるたぬき.（ゴールド）",
"48.気ままなチーター.（シルバー）",
"49.楽天的な虎.（ブルー）",
"50.スタイリッシュな黒ひょう.（パープル）",
"51.完璧主義なライオン.（イエロー）",
"52.職人気質なライオン.（グリーン）",
"53.創造的な黒ひょう.（レッド）",
"54.許容力のある虎.（オレンジ）",
"55.リーダー的な虎.（ブラウン）",
"56.好奇心旺盛な黒ひょう.（ブラック）",
"57.白黒つけたがるライオン.（ゴールド）",
"58.先見の明があるライオン.（シルバー）",
"59.平和主義な黒ひょう.（ブルー）",
"60.自分の世界を持った虎.（パープル）"
]

fate_num = gap_days % 60

result_animal = animal_list[fate_num]


'''
#### 動物占いの結果は...
'''
st.write(result_animal)

'''
#### あなたにオススメの和菓子は...
'''

wagashi_list = [
    "「清浄歓喜団」 （唐菓子）京都・亀屋清永",
    "「関の戸」（求肥とこしあん 忍者） 三重 関宿・深川屋陸奥大掾",
    "「夜の梅」（小倉羊羹）とらや",
    "「いろこおり」 （氷菓子） 池袋西武・かしこと",
    "「あまのはら」 （四季の富士山） 新宿・ 和菓子 結",
    "「二人静」（和三盆） 名古屋・両口屋是清",
    "「どらやき」（どらやきの元祖） 京都・笹屋伊織",
    "「ハーブのらくがん」東京・wagashi asobi", 
    "「あんわらび」（こしあん × わらびもち）東京・成城あんや",
    "「一◯香（いっこっこう）」 （びっくりする焼き菓子） 長崎・茂木一まる香本家",
    "「空也もなか」 銀座・空也",
    "「万葉の花」（生落雁） 金沢・諸江屋"
]

result_sweets = wagashi_list[fate_num % 12]

st.write(result_sweets)


# 清浄歓喜団 https://kameyakiyonaga.co.jp/year01.html
# 関の戸 http://www.sekinoto.com/
# あまのはら http://www.wagashi-yui.tokyo/
# 
# 一◯香 https://mogi105.com/c-item-detail?ic=0001-01


links = [
    '[清浄歓喜団](https://kameyakiyonaga.co.jp/year01.html)',
    '[関の戸](http://www.sekinoto.com/)',
    '[夜の梅](https://www.toraya-group.co.jp/toraya/products/yokan/yokan-yorunoume/)',
    '[いろこおり](https://www.ozmall.co.jp/temiyage/article/24305/)',
    '[あまのはら](http://www.wagashi-yui.tokyo/wagashi/amanohara.html)',
    '[二人静](https://ryoguchiya-korekiyo.co.jp/products/nininsizuka/)',
    '[どらやき](https://www.sasayaiori.com/dorayaki/)',
    '[ハーブのらくがん](https://wagashi-asobi.com/item/item_b.html)',
    '[あんわらび](http://www.seijoanya.com/nama.html)',
    '[一◯香](https://mogi105.com/c-item-detail?ic=0001-01)',
    '[空也もなか](https://www.wagashi.or.jp/tokyo_link/shop/0337.htm)',
    '[万葉の花](https://moroeya.net/?pid=7218034)',
]

link = '[清浄歓喜団](https://kameyakiyonaga.co.jp/year01.html)'
st.markdown(links[fate_num % 12], unsafe_allow_html=True)

if (fate_num % 12) == 0:
    st.image("SeijoKankidan_KameyaYoshinaga.png")

##
# End of This File
##
