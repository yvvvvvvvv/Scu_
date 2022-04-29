from turtle import width
from PIL import Image
import os

print(f"Current working dir: {os.getcwd()}")
print(os.path.join(os.getcwd(),'yu.jpg'))

a = Image.open(os.path.join(os.getcwd(),'yu.jpg'))

w, h = a.size
a1 = a.resize((int(w*1.2),h))
a2 = a.resize((int(w*1.5),h))
a3 = a.resize((int(w*0.5),h))
a4 = a.resize((int(w*0.8),h))

a1.save('yu1.jpg')
a2.save('yu2.jpg')
a3.save('yu3.jpg')
a4.save('yu4.jpg')
