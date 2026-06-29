# Jarvis - Voice Activated Virtual Assistant

A voice-activated virtual assistant built with Python that responds to voice commands.

## Features
- Wake word detection ("Jarvis")
- Opens websites via voice (YouTube, Google, GitHub)
- Plays music from your personal library
- Reads latest technology news headlines
- Text-to-speech responses

## Libraries Used
- `pyttsx3` - Text to speech
- `speech_recognition` - Voice to text
- `webbrowser` - Opening websites
- `requests` - Fetching news from API
- `python-dotenv` - Secure API key management

## Setup
1. Clone the repository
2. Create a virtual environment: `virtualenv env`
3. Activate it: `source env/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.env` file and add your NewsAPI key: `NEWS_API_KEY=your_key`
6. Run: `python main.py`

## Usage
- Say **"Jarvis"** to activate
- Say **"open YouTube/Google/GitHub"** to open websites
- Say **"play [song name]"** to play music
- Say **"news"** to hear latest headlines