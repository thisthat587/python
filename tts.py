import sys
import os

try:
    from gtts import gTTS
except ImportError:
    os.system('pip install gtts')
    from gtts import gTTS

import pygame

def text_to_speech(text):
    # Create a gtts object
    tts = gTTS(text=text, lang='en')

    # Save the speech as an MP3 file
    tts.save('output.mp3')

    # Play the MP3 file using pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    pygame.time.Clock().tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    # Read text from stdin
    text_input = sys.stdin.readline().strip()

    # Convert text to speech and play it
    text_to_speech(text_input)
