# pip install pyqrcode
# pip install pypng

import pyqrcode
import png

print("Please Enter Your Name: ")
name =input()

QRstring= f'This is {name} Account'

url= pyqrcode.create(QRstring)

url.png('qr.png', scale=8)

input()