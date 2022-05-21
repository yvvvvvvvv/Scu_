from PIL import Image
import pytesseract
import matplotlib.pyplot as plt
import os

plt.imshow(Image.open(os.path.join(os.getcwd(),'170542.jpg')))
plt.show()

text = pytesseract.image_to_string('170542.jpg')
print(text)