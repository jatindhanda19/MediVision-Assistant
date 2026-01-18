"""
step1: Auto Recorder using Microphone

This script records audio from user's microphone ,
converts it to mp3 using ffmpeg , and saves locally.

Requirements:
-ffmpeg installed
-portaudio installed
-pydub
-speech recognition
"""

import logging
from pydub import AudioSegment
from io import BytesIO
import speech_recognition as sr

# Path to ffmpeg executable (change this according to your system)
AudioSegment.converter = r"C:\Users\sam\Downloads\ffmpeg\bin\ffmpeg.exe"

# Configure logging for better debugging and visibility
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path="patient_voice.mp3", timeout=20, phrase_time_limit=None):
    """
    Record audio from the microphone and save it as an MP3 file.

    parameters:
    -file_path : output file name
    -timeout: Max seconds to wait for speech
    -phrase time limit : max duration of recording
    """
    recognizer = sr.Recognizer()

    try:
        # Use microphone as source
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            # Record audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            # Convert to MP3 using pydub
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# 🔹 Run the function
if __name__ == "__main__":
   audio_filepath = "patient_voice.mp3"
   record_audio(file_path=audio_filepath)


"""
Step 2: Speech to text (STT) using Groq Whisper API

this script uploads the recorded mp3 file to Groq's
Whisper Large V3 model and returns the transcription

Requirement:
-grok SDK
-python dotenv
-GROQ_API_KEY set in environment variables
"""

import os
from dotenv import load_dotenv
from groq import Groq

# load environment variables from .env file
load_dotenv()

# Fetch Groq API key securely
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

# Whisper STT model
stt_model = "whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    """
    sends audio file to Groq Whisper API and returns transcription text.

    parameters:
    -stt_model : Whisper model name
    -audio_filepath: path to audio file
    -api_key: Groq API key

    Returns:
    -str: Trancribed text
    """
    client = Groq(api_key=GROQ_API_KEY)
    with open(audio_filepath,"rb")as audio_file:
        transcription = client.audio.transcriptions.create(
          model=stt_model,
          file=audio_file,
          language="en"
    
    )
    return transcription.text

