import sys
from gtts import gTTS
import os

text = sys.stdin.readline().strip()
# text='hello'
tts = gTTS(text, lang='en')
tts.save('output.mp3')
os.system('mpg123 output.mp3')
