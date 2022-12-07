import pyttsx3
import PyPDF2


def text-speech(pdf):
    book=open(pdf,'rb')
    pdfReader=PyPDF2.PdfFileReader(book)

    count=pdfReader.numPages
# print(count)
   speaker=pyttsx3.init()
# for num in range(0,count):
#     page=pdfReader.getPage(num)
#     text=page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()



# page=pdfReader.getPage(3)
# text=page.extractText()
# speaker.say(text)
# speaker.runAndWait()