import pyttsx3
import PyPDF2
from tkinter.filedialog import *

PDFname = askopenfilename()
PDFreader = PyPDF2.PdfReader(PDFname)
nopages = len(PDFreader.pages)

for i in range(0,nopages):
    page = PDFreader.pages[i]
    texts = page.extract_text()
    voicePlayer = pyttsx3.init()
    voicePlayer.setProperty('rate',180)
    voicePlayer.setProperty('volume',10.0)
    voicePlayer.say(texts)
    voicePlayer.runAndWait()