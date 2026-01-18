# step1 a: Setup text to speech TTS-model with gTTS 
import os 
from dotenv import load_dotenv

load_dotenv()
from gtts import gTTS

def text_to_speech_with_gtts(input_text,output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang= language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text = "what is red?"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="final.mp3")

# step1 b: Setup text to speech TTS-model with Elevenlabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY= os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text,output_filepath):
    client= ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        text =input_text,
        voice_id ="XrExE9yKIg1WjnnlVkGX",
    )
    elevenlabs.save(audio,output_filepath)
input_text = "what is red eye ?"
#text_to_speech_with_elevenlabs(input_text,output_filepath="final_eve.mp3")
# step2 Use Model for text output to voiceimport subprocessimport platform def text_to_speech_with_gtts(input_text,output_filepath):    language="en"    audioobj = gTTS(        text= input_text,        lang = language,        slow=False    )    audioobj.save(output_filepath)    os_name = platform.system()        try:        if os_name == "Darwin":            subprocess.run(['afplay',output_filepath])        elif os_name == "Windows":             os.startfile(os.path.abspath(output_filepath))                        elif os_name == "Linux":            subprocess.run(['mpg123',output_filepath])        else:            raise OSError("unsupported operating system")    except Exception as e:        print(f"An error occurred while trying to play:{e}")input_text = "Why my arm is red auto"#text_to_speech_with_gtts(input_text,output_filepath="gtts_testing_auto.mp3")#Elevenlabs import elevenlabsfrom elevenlabs.client import ElevenLabsELEVENLABS_API_KEY= os.environ.get("ELEVENLABS_API_KEY")def text_to_speech_with_elevenlabs(input_text,output_filepath):    client= ElevenLabs(api_key=ELEVENLABS_API_KEY)    audio = client.text_to_speech.convert(        text =input_text,        voice_id ="Xb7hH8MSUJpSbSDYk0k2",    )    elevenlabs.save(audio,output_filepath)    os_name = platform.system()        try:        if os_name == "Darwin":            subprocess.run(['afplay',output_filepath])        elif os_name == "Windows":             os.startfile(os.path.abspath(output_filepath))                        elif os_name == "Linux":            subprocess.run(['mpg123',output_filepath])        else:            raise OSError("unsupported operating system")    except Exception as e:        print(f"An error occurred while trying to play:{e}")input_text = "Why my arm is red auto"#text_to_speech_with_elevenlabs(input_text,output_filepath="eleven_testing_auto.mp3")

import subprocess
import platform

def text_to_speech_with_gttsold(input_text,output_filepath):
    language="en"

    audioobj=gTTS(
        text=input_text,
        lang= language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin": #macOS
            subprocess.run('asplay',output_filepath)
        elif os_name == "Windows": #Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux": #Linux
            subprocess.run(['mpg123',output_filepath])
        else:
            raise OSError("unsupported operating system")
    except Exception as e:
        print(f'An error occured')

input_text = "what is dandruff?"
text_to_speech_with_gttsold(input_text=input_text, output_filepath="final.mp3")

