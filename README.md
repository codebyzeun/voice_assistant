# Voice Assistant

A simple voice assistant built with Python that can respond to commands, manage tasks, and more. It’s a work in progress but aims to help you automate simple tasks using voice commands.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/voice_assistant.git
   ```
2. Navigate into the project directory:
   ```
   cd voice_assistant
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
## Usage

Run the assistant with:
```
python main.py
```
The assistant will start listening for commands. Make sure your microphone is set up and ready to use. Speak your command, and the assistant will respond accordingly.

## Project Structure

```
voice_assistant/
├── commands/           # Contains the code for different voice commands and actions
├── config/             # Configuration files and settings for the assistant
├── logs/               # Logs for tracking assistant activity and errors
├── utils/              # Utility functions for speech recognition, text-to-speech, etc.
├── main.py             # Main entry point for running the assistant
└── requirements.txt    # Python dependencies for the project
```

## Korean Language Setup

Since this assistant is designed to work with Korean voice commands, you must ensure that the Korean language is set up correctly for both speech recognition and text-to-speech. Here's how:

1. Install the Korean Language Pack on Windows
Follow these steps to add the Korean language and voice on your Windows PC:
   1. Go to Settings > Time & Language > Language
   2. Add Korean as a language (if it’s not already added)
   3. Under Speech, ensure the Korean voice is installed and available
   4. Restart your PC after adding the language pack to ensure everything works properly

2. Install the Required Python Packages
The assistant uses the ``speech_recognition`` library to handle speech-to-text (STT) and pyttsx3 for text-to-speech (TTS). Install these packages by running: bash Copy Edit
   ```
   pip install SpeechRecognition pyaudio pyttsx3
   ```

3. Speech Recognition (STT) Setup
The assistant uses Google's Speech Recognition API to handle voice commands in Korean. It automatically recognizes commands spoken in Korean ``(ko-KR)``. No additional configuration is needed for this if you have a working microphone.

4. Text-to-Speech (TTS) Setup
The assistant uses ``pyttsx3`` for text-to-speech. The system’s installed voices are used, and it will attempt to use the Korean voice if available.

If the Korean voice is detected on your system, the assistant will automatically set it for speaking Korean responses. This is done using the following code in ``main.py``:

```
voices = engine.getProperty('voices')
korean_voice = None
for voice in voices:
    if 'korean' in voice.name.lower():
        korean_voice = voice
        break
if korean_voice:
    engine.setProperty('voice', korean_voice.id)
```
If the Korean voice is not available, it will fall back to the default system voice.

5. Set Korean as the Default Language in Code
The speech recognition and TTS are configured to use the Korean language by default in the code. You don’t need to modify any of the settings, as they are pre-configured to handle Korean.

# Contributing

Feel free to contribute to this project!
