import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog

# create a new SpeechRecognition instance
r = sr.Recognizer()

# create a GUI window using tkinter
window = tk.Tk()

# define a function to handle the drag and drop event
def handle_drop(event):
    # get the file path from the dropped event
    file_path = event.data['text'].replace('file:///', '/')

    # load the audio file
    with sr.AudioFile(file_path) as source:
        # read the audio data from the file
        audio_data = r.record(source)

    # use Google Speech Recognition to convert the audio to text
    text = r.recognize_google(audio_data)

    # print the text
    print(text)

# create a label in the GUI window to indicate where to drop the file
label = tk.Label(window, text="Drag and drop an audio file here")
label.pack(pady=20)

# bind the handle_drop function to the drag and drop event
window.bind('<Drop>', handle_drop)

# run the GUI window
window.mainloop()
