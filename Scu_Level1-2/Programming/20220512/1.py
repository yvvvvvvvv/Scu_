from base64 import encode
import jieba
from wordcloud import WordCloud

with open("text17_29.txt",encoding="utf-8") as fp:
    txt = fp.read()

cut_text = ' '.join(jieba.cut(txt))

wd = WordCloud(font_path="C:/Windows/Fonts\mingliu", background_color='white',width=1000,height=880).generate(cut_text)

i = wd.to_image()
i.show()