from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import jieba
import numpy as np

with open("text17_29.txt", encoding="utf-8") as fp:
    txt = fp.read()
cut_text = ' '.join(jieba.cut(txt))

b = np.array(Image.open('s.jpg'))

wd = WordCloud(font_path='C:/Windows/Fonts\mingliu', background_color='White', mask=b).generate(cut_text)

plt.imshow(wd)
plt.axis('off')
plt.show()