import speech_recognition as sr
import pyttsx3
import datetime
import json
import os
import re
import webbrowser
from time import sleep

from commands import time, weather, music, jokes, timer, calculator, game, quote, news
from utils import speech, tts

recognizer = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')

korean_voice = None
for voice in voices:
    if 'korean' in voice.name.lower():
        korean_voice = voice
        break

if korean_voice:
    engine.setProperty('voice', korean_voice.id)
    print(f"Korean Voice: {korean_voice.name}")
else:
    print("Korean voice not found, using default voice.")

engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


def load_settings():
    if os.path.exists("config/settings.json"):
        with open("config/settings.json", "r") as file:
            return json.load(file)
    return {}

def handle_invalid_command():
    tts.speak("죄송합니다. 이해하지 못했습니다. 다시 말씀해 주세요.")

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

def run_command(command):
    if 'time' in command:
        return time.get_current_time()
    elif 'weather' in command:
        return weather.get_weather()
    elif 'music' in command:
        return music.play_music()
    elif 'joke' in command:
        return jokes.tell_joke()
    elif 'timer' in command:
        duration = int(re.search(r'\d+', command).group())
        return timer.set_timer(duration)
    elif 'calculate' in command or 'math' in command:
        expression = re.sub(r"[^0-9+\-*/(). ]", "", command)
        return calculator.calculate(expression)
    elif 'rock' in command or 'paper' in command or 'scissors' in command:
        choice = [word for word in command.split() if word in ["rock", "paper", "scissors"]]
        if choice:
            return game.play_rps(choice[0])
        else:
            return "Please choose rock, paper, or scissors."
    elif 'quote' in command:
        return quote.get_quote()
    elif 'news' in command:
        return news.get_news()
    elif 'open' in command or 'go to' in command:
        match = re.search(r'(open|go to)\s(.*)', command)
        if match:
            website = match.group(2)
            return open_website(website)
        else:
            return "Please specify a website to open."
    elif 'hello' in command or 'hi' in command:
        return "안녕하세요! 저는 당신의 비서입니다."
    elif 'goodbye' in command or 'exit' in command:
        return "안녕히 가세요! 좋은 하루 되세요."
    else:
        return None

def open_website(website):
    if "https" not in website:
        website = "https://" + website
    tts.speak(f"{website}를 엽니다.")
    webbrowser.open(website)
    return f"Opening {website} in your browser."


def main():
    settings = load_settings()

    tts.speak("안녕하세요! 저는 당신의 비서입니다. 어떻게 도와드릴까요?")

    while True:
        try:
            audio = listen_for_command()
            command = speech.recognize_speech(audio).lower()
            print(f"You said: {command}")

            response = run_command(command)

            if response:
                tts.speak(response)
            else:
                handle_invalid_command()

            if 'goodbye' in command or 'exit' in command:
                break

        except sr.UnknownValueError:
            handle_invalid_command()
        except sr.RequestError:
            tts.speak(
                "죄송합니다. 음성 인식 서비스에 오류가 발생했습니다.")
        except Exception as e:
            print(f"An error occurred: {e}")
            tts.speak("예기치 않은 오류가 발생했습니다.")
        sleep(1)

if __name__ == "__main__":
    main()
