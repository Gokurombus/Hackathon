from tkinter.filedialog import *
import pytesseract
import random
image = askopenfilename()

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\user\\Downloads\\tesseract"

text = pytesseract.image_to_string(image)
print(text)
x=str(random.random())
with open("text_file"+x+".txt" , "w+") as f:
    f.write(text)
