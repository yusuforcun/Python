# Importing library
import pyqrcode

# Data to be encoded
data = 'https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/'

# Encoding data using make() function
img = pyqrcode.create(data)
# Saving as an image file
img.save()
