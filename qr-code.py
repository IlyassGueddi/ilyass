import qrcode
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=1,  # controls size (1 is smallest, 40 is largest)
    error_correction=ERROR_CORRECT_H,  # how much damage can be tolerated
    box_size=10,  # size of each “box” in pixels
    border=4,     # thickness of border (in boxes)
)

source = input("what you want to encode: ")

qr.add_data(source)  # what to encode
qr.make(fit=True)
 
img = qr.make_image(fill_color="black", back_color="white")
img.save("github.png")
