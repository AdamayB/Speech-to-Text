import speech_recognition as sr
import pyttsx3
r1= sr.Recognizer()
sr.Microphone.list_microphone_names()
while True:
    try:
        with sr.Microphone() as mic:
            r1.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r1.listen(mic)
            text = r1.recognize_google(audio)
            print(f"Recognised text={text}")


    except sr.UnknownValueError:
        r1 = sr.Recognizer()
        continue
