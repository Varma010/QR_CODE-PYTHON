from pyqrcode import QRCode
data=input("enter data here:")
img=QRCode(data)
img.png("qrcode.png",scale=12)
