import imp
from PIL import Image
from PIL import ImageColor

a = Image.new('RGBA',(300,300),'Thistle')
for x in range(50,251):
    for y in range(50,151):
        a.putpixel((x,y), (126,150,137,255))
a.save('i.png')