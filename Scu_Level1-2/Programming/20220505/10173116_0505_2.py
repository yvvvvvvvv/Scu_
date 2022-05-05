from turtle import width
from PIL import Image
import os

#print(f"Current working dir: {os.getcwd()}")
print(os.path.join(os.getcwd(),'a.jpg'))

a = Image.open(os.path.join(os.getcwd(),'a.jpg'))
b = a.copy()
c = b.crop((502,110,582,190)) #80 X 80
w, h = c.size

n = Image.new('RGB', (680,360), 'Tan')
for x in range(20, 660, w):
    for y in range(20, 340, h):
        n.paste(c, (x,y))
n.save('i.jpg')