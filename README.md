# QR_CODE-PYTHON
QRCODE GENARATOR AND READER WITH PYQRcode AND CV2
____________________________________________________
Generate QR code image with Python, Pillow, qrcode
____________________________________________________

You can easily generate QR code images using Python's QR code generation library "qrcode". It is also possible to embed a QR code in another image or embed an image in a QR code using Pillow.

Here, the following contents will be described.

    Python QR Code image generator: qrcode
    Generate QR code image from the command line
    Generate QR code image with Python code
        QR code version of the generated image: version
        Error correction level: error_correction
        Cell size: box_size
        Margin width: border
        Color: fill_color, back_color
    Embed the QR code into the image
    Embed the image into the QR code
    
    
    
# Requirements

The pyqrcode module only requires Python 2.6, Python 2.7, or Python 3.
You may want to install pypng in order to render PNG files, but it is optional. 
Note, pypng is a pure python PNG writer which does not require any other library.

$ pip3 install pypng

$ pip3 install pyzbar

# Installation

Installation is simple. It can be installed from pip using the following command:

$ pip install pyqrcode

Or from the terminal:

$ python setup.py install



