
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import os
from musicLibrary import music
from google import genai

# Initialize speech recognition and Gemini
recognizer = sr.Recognizer()
client = genai.Client()

# Speak a message
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print(text)


# Listen to the user's voice
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        text = text.lower().strip()
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand the audio. Please try again.")
        return ""

    except sr.RequestError as e:
        print("Speech recognition service error:", e)
        return ""


# Fetch news from NewsAPI
def get_news():
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        speak("News API key is missing.")
        return

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": "India",
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            speak("Sorry Boss, no news articles were found.")
            return

        for article in articles[:5]:
            title = article.get("title")

            if title:
                speak(title)

    except requests.RequestException as e:
        print("News API error:", e)
        speak("Sorry Boss, I couldn't fetch the news.")


# Ask Gemini a question
def ask_ai(question):
    try:
        response = client.models.generate_content(
            model="gemma-4-31b-it",
            contents=question
        )

        answer = response.text

        if answer:
            speak(answer)
        else:
            speak("Sorry Boss, I couldn't generate an answer.")

    except Exception as e:
        print("AI request failed:", e)
        speak("Sorry Boss, I couldn't get an answer right now.")


# Main Jarvis program
if __name__ == "__main__":
    speak("Initializing Jarvis.")

    while True:
        command = listen()

        # Wait for the wake word
        if "jarvis" in command:
            speak("Yes Boss")

            a = listen()

            if not a:
                continue

            # Open websites
            if "google" in a:
                webbrowser.open("https://www.google.com/")

            elif "youtube" in a:
                webbrowser.open("https://www.youtube.com/")

            elif "facebook" in a:
                webbrowser.open("https://www.facebook.com/")

            elif "linkedin" in a:
                webbrowser.open("https://www.linkedin.com/")

            # Fetch news
            elif "news" in a:
                get_news()

            # Play a song from the music library
            elif "play" in a or any(song in a for song in music):
                song_found = False

                for song in music:
                    if song in a:
                        webbrowser.open(music[song])
                        song_found = True
                        break

                if not song_found:
                    speak("Sorry Boss, that song is not in your music library.")

            # Send other questions to Gemini
            else:
                ask_ai(a)