# Jarvis Voice Assistant

A Python-based voice assistant project inspired by virtual assistants like Jarvis.

## Features

* Voice input using speech recognition
* Voice responses using text-to-speech
* Open websites using voice commands
* Play songs using a music library
* Fetch news using NewsAPI
* Answer questions using Gemini AI

## Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* Requests
* Google Gemini API
* NewsAPI

## Requirements

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

You also need:

* A working microphone
* An internet connection
* A NewsAPI key
* A Gemini API key

## API Keys

The project uses environment variables for API keys.

Configure the following environment variables on your computer:

```text
NEWS_API_KEY
GEMINI_API_KEY
```

Never write your actual API keys directly inside the Python source code or upload them to GitHub.

## How to Run

1. Install Python.
2. Install the required packages.
3. Configure your API keys.
4. Run the main Python file:

```bash
python main.py
```

---

# User Guide

## 1. Start Jarvis

Run:

```bash
python main.py
```

Jarvis will start by saying:

> Initializing Jarvis.

After starting, Jarvis continuously listens for the wake word.

---

## 2. Wake Jarvis

Say:

```text
Jarvis
```

When Jarvis detects the word `jarvis`, it responds:

```text
Yes Boss
```

Jarvis then listens for the next command.

### Basic flow

```text
User: Jarvis
       ↓
Jarvis: Yes Boss
       ↓
Jarvis listens for a command
       ↓
Command is checked
       ↓
Action is performed
```

---

# Available Commands

## 🌐 3. Open Google

First say:

```text
Jarvis
```

Jarvis responds:

```text
Yes Boss
```

Then say something containing:

```text
Google
```

For example:

```text
Open Google
```

### What happens?

Jarvis opens:

```text
https://www.google.com/
```

in your default web browser.

---

## ▶️ 4. Open YouTube

Say:

```text
Jarvis
```

Then:

```text
Open YouTube
```

### What happens?

Jarvis opens YouTube in your default web browser.

---

## 📘 5. Open Facebook

Say:

```text
Jarvis
```

Then:

```text
Open Facebook
```

### What happens?

Jarvis opens Facebook in your default web browser.

---

## 💼 6. Open LinkedIn

Say:

```text
Jarvis
```

Then:

```text
Open LinkedIn
```

### What happens?

Jarvis opens LinkedIn in your default web browser.

---

# 🎵 7. Play Music

Music is stored in the `musicLibrary.py` file.

For example, the music library can contain songs such as:

```text
Ijazat
Admiring You
Tune Jo Na Kaha
```

Say:

```text
Jarvis
```

Then say:

```text
Play Ijazat
```

### What happens?

Jarvis checks the command against the songs stored in `musicLibrary.py`.

If the song is found, Jarvis opens the YouTube link associated with that song.

### Important

The song must exist in the `musicLibrary.py` music dictionary.

If the requested song is not in the library, Jarvis says:

```text
Sorry Boss, that song is not in your music library.
```

---

# 📰 8. Get News

Say:

```text
Jarvis
```

Then say:

```text
News
```

### What happens?

Jarvis calls the NewsAPI service.

The program:

1. Gets the `NEWS_API_KEY` from the environment.
2. Sends a request to NewsAPI.
3. Searches for India-related news.
4. Sorts the results by publication time.
5. Receives the response as JSON.
6. Extracts the article titles.
7. Reads up to 5 article titles aloud.

### Example flow

```text
User: Jarvis
       ↓
Jarvis: Yes Boss
       ↓
User: News
       ↓
Jarvis → NewsAPI
       ↓
NewsAPI → JSON response
       ↓
Jarvis extracts article titles
       ↓
Jarvis reads the titles aloud
```

If no articles are found, Jarvis says:

```text
Sorry Boss, no news articles were found.
```

If the NewsAPI request fails, Jarvis says:

```text
Sorry Boss, I couldn't fetch the news.
```

---

# 🤖 9. Ask Gemini AI

If the command does not match Google, YouTube, Facebook, LinkedIn, News, or a song in the music library, Jarvis sends the command to the AI function.

For example:

```text
Jarvis
```

Jarvis responds:

```text
Yes Boss
```

Then ask:

```text
What is machine learning?
```

### What happens?

The question is sent to the Gemini API.

The AI generates an answer, and Jarvis speaks the answer using text-to-speech.

### AI flow

```text
Your voice
    ↓
Speech Recognition
    ↓
Text
    ↓
Jarvis checks fixed commands
    ↓
No matching command
    ↓
Gemini AI
    ↓
AI-generated answer
    ↓
Text-to-Speech
    ↓
Jarvis speaks the answer
```

---

# 🗣️ 10. Speech Recognition

Jarvis uses the `SpeechRecognition` library to convert your voice into text.

The basic process is:

```text
Your voice
    ↓
Microphone
    ↓
SpeechRecognition
    ↓
Recognized text
    ↓
Jarvis processes the command
```

If Jarvis cannot understand the audio, it prints:

```text
Could not understand the audio. Please try again.
```

If the speech recognition service has an error, Jarvis displays the error and returns an empty command.

---

# 🔊 11. Text-to-Speech

Jarvis uses `pyttsx3` to speak responses.

For example:

```text
Initializing Jarvis.
```

and:

```text
Yes Boss
```

are converted from text into speech.

The basic process is:

```text
Text
 ↓
pyttsx3
 ↓
Computer speaker
 ↓
Jarvis speaks
```

---

# 🔄 Complete Jarvis Workflow

The complete program works approximately like this:

```text
Start Program
      ↓
Initializing Jarvis
      ↓
Listen for Wake Word
      ↓
Did Jarvis hear "Jarvis"?
      │
      ├── No → Continue listening
      │
      └── Yes
            ↓
        "Yes Boss"
            ↓
       Listen to command
            ↓
      ┌─────┴─────────────────────────┐
      ↓                               ↓
 Fixed command?                    No match
      ↓                               ↓
 ┌────┼────┬────┬────┬────┐       Gemini AI
 ↓    ↓    ↓    ↓    ↓    ↓          ↓
Google YouTube Facebook LinkedIn News Music
 ↓    ↓    ↓    ↓    ↓    ↓          ↓
Open browser / perform action     Speak answer
```

---

# 📁 Project Structure

```text
Mega project - Jarvis/
│
├── main.py
├── musicLibrary.py
├── openai_test.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `main.py`

Contains the main Jarvis program, including:

* Speech recognition
* Text-to-speech
* Wake-word detection
* Website commands
* News fetching
* Music commands
* Gemini AI integration

### `musicLibrary.py`

Contains the music dictionary and YouTube links used by Jarvis for music playback.

### `requirements.txt`

Contains the Python packages required to run the project.

### `README.md`

Contains information about the project, installation, features, and user guide.

### `.gitignore`

Contains files and folders that should not be uploaded to GitHub, such as the Python virtual environment and cache files.

---

# ⚠️ Important Notes

* Jarvis requires a working microphone.
* An internet connection is required for speech recognition, NewsAPI, and Gemini AI.
* Music commands depend on the songs available in `musicLibrary.py`.
* News requires a valid `NEWS_API_KEY`.
* AI questions require a valid Gemini API key.
* API keys should never be written directly into the source code.
* Do not upload API keys to GitHub.

---

# 🚧 Project Status

This project is under development as I learn Python and build my own voice assistant.

More commands and features will be added in the future.
