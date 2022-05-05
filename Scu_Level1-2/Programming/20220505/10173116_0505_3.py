from PIL import Image, ImageDraw, ImageFont

n = Image.new('RGBA', (300,300), "Rosybrown")
d = ImageDraw.Draw(n)

d.rectangle((0,0,299,299), outline='Silver')
#d.ellipse((45,90,75,120), outline='Black')
d.ellipse((50,95,70,115), fill='Paleturquoise')
#d.ellipse((225,90,255,120), outline='Black')
d.ellipse((230,95,250,115), fill='Paleturquoise')
d.polygon([(150,120),(180,180),(120,180),(150,120)], fill='Indianred')
d.rectangle((90,210,210,215), fill='Ivory')

s = 'Hello Everyone...'
f = ImageFont.truetype('C:\Windows\Fonts\BRADHITC.TTF', 28)
d.text((55,260), s, fill='Lavender', font=f)

n.save('i.png')