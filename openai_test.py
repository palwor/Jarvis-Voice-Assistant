import speech_recognition as sr
import pyttsx3
from google import genai
recognizer = sr.Recognizer()

def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()
  print(text)


def listen():
  try:
    with sr.Microphone() as source:
      print("listenning.....")                
      audio = recognizer.listen(source)                   
      text =recognizer.recognize_google(audio)
      l=text.lower() 
      print(l)
    return l
  except sr.UnknownValueError as e:
    print("Google Speech Recognition could not understand audio")
    return listen()
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return "speech service unavailable"
client = genai.Client()

question = listen()

response = client.models.generate_content(
    model="gemma-4-31b-it",
    contents=question
)

print(response.text)
58e9e7aec82548d5adca83fca9393fb2