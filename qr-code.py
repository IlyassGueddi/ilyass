import qrcode
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,     
)

source = input("what you want to encode: ")

qr.add_data(source)
qr.make(fit=True)
 
img = qr.make_image(fill_color="black", back_color="white")
img.save("github.png")
