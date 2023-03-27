import speech_recognition as sr

r = sr.Recognizer()

# load the audio file
with sr.AudioFile("path/to/audio/file.wav") as source:
    audio_data = r.record(source)

# use Google Speech Recognition to convert the audio to text
text = r.recognize_google(audio_data)

print(text)
