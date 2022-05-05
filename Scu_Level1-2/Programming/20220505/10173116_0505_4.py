import qrcode
from PIL import Image

qr=qrcode.QRCode(version=5,
                 error_correction=qrcode.constants.ERROR_CORRECT_M,
                 box_size=10,
                 border=4)
qr.add_data("早柚參上")
img=qr.make_image(fill_color='Green')
width,height=img.size
with Image.open("yu.jpg") as obj:
    obj_width,obj_height=obj.size
    new_obj=obj.resize((obj_width//2,obj_height//2))
    obj_width,obj_height=new_obj.size
    img.paste(new_obj,((width-obj_width)//2,(height-obj_height)//2))
img.save("i.jpg")
        
