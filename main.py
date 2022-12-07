#  Required Module is imported for text to voice conversion
from gtts import gTTS
#  below module is imported so that we can play audio , by using os module
import os 

def text_to_speech(tex,voice):
    output=gTTS(text=tex, lang=voice, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")





# #  in myText we can any language text to convert into audio 
# myText="शी जिनपिंग सरेआम कनाडा के पीएम जस्टिन ट्रूडो पर क्यों झल्लाए, पश्चिमी मीडिया ने बताई वजह"

# # select the language of audio
# language="hi"

# # 'en'--- for english
# #  'hi'--- for hindi
# #  'bn'--- for bengali
# # Assamese	as
# # Oriya	or

# #  processing of text, here we pass the the text and language to engine and slow the speed of voice
# output=gTTS(text=myText, lang=language, slow=False)


# #  saving  the converted audio  into  mp3 file
# output.save("output.mp3")

# #  playing the audio file
# os.system("start output.mp3")