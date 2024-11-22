import webbrowser
import speech_recognition as sr

r=sr.Recognizer()
def speech_recognition():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Lisening.....")
        audio=r.listen(source)
        print("Recognising.....")
        try:
            dest=r.recognize_google(audio)
            print(dest,".....")
            path="https://www.google.com/search?q="+dest
            print(webbrowser.open(path))
        except sr.UnknownValueError:
            print("Unable to Recognise..")
        except sr.RequestError as e:
            print("Error:", e)

speech_recognition()