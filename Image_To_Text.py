from tkinter.filedialog import *
import pytesseract
image = askopenfilename()

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\user\\Downloads\\tesseract"

text = pytesseract.image_to_string(image)
print(text)

with open("text_file.txt" , "w+") as f:
    f.write(text)