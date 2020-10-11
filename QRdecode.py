from pyzbar.pyzbar import decode
from PIL import Image
data=decode(Image.open('qrcode.png'))
print(data)
