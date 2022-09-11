from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('file path + image name')

result = decode(img)
print(result)