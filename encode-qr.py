import qrcode

data = 'chapchap login'

# img = qrcode.make(data)
# img.save('/home/vanessa/Documents/python/qr-code/myqr.png')

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = 'pink', back_color = 'yellow')
img.save('file path + image name')