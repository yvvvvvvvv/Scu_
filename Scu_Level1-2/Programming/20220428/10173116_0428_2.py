from turtle import width
from PIL import Image
import os

print(f"Current working dir: {os.getcwd()}")
print(os.path.join(os.getcwd(),'yu.jpg'))

a = Image.open(os.path.join(os.getcwd(),'yu.jpg'))
b = a.copy()
c = b.crop((100,40,185,130))
#c.save('i.jpg')
b.paste(c,(0,0))
b.paste(c,(214,0))
b.paste(c,(0,78))
b.paste(c,(214,78))
b.save('i.jpg')