from playsound import playsound as ps
import os
from gtts import gTTS
import time

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def speak(text, filename="out.mp3"): #take in text to speak and a filename to save it under
    if filename[-4:] != ".mp3": #so i don't have to add .mp3 to the end of every file
        filename = filename + ".mp3"
    
    try: #in case the file  doesnt exist, to prevent errors
        os.remove(f"sounds/{filename}") #in case the file exists, to prevent errors
    except:
        pass
    
    try:
        audio = gTTS(text) #convert text parameter to audio
        audio.save(f"sounds/{filename}") #save converted audio
    except(AssertionError):
        return None

    ps(f"sounds/{filename}", False)
    
    
def read(img): #take in image to read
    text = pytesseract.image_to_string((img), lang="eng.undertale") #use tesseract to convert image text to string
    if len(text) > 0 and text[0] == "*": #remove asterisk at start of text
        text = text[1:]
    return text
