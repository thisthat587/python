# tts.py
import sys
import pyttsx3

text = sys.stdin.readline().strip()

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
