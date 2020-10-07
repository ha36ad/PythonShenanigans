import pytesseract as tess
from PIL import Image

#Enter your tesseract directory here
tess.pytesseract.tesseract_cmd = r''

#Open the image
img = Image.open('text.png')

#Saving the output in a variable
text =tess.image_to_string(img)

#Printing the output
print(text)
