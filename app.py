"""
ARTIFICIAL DOCTOR - VOICE & VISION MEDICAL ASSISTANT

This  Gradio application allows a user to:
1.Speak their medical concern
2.Upload an image (face/ skin/etc.)
3.Receive a medical-style response
4.Hear the doctor's voice reply
"""

import os
import gradio as gr
import time 
import uuid

# Import internal modules
from Brain_of_doctor import encode_image, analyze_image_with_query
from voice_of_patient import record_audio, transcribe_with_groq
from voice_of_doctor  import text_to_speech_with_elevenlabs, text_to_speech_with_gtts

# System prompt (Doctor Personality & Rules)
system_prompt="""You have to act like doctor, i know you are not but for learning purpose.  what is in the image?. Do you find anything wrong with it medically?
               If you make a differential,suggest some remedies for them.Donot add any number or special characters in
               your response.Your response should be in one long paragraph.Also always answer as if you are answering to 
               real person. Donot say 'In the image I see' but say'with what I see,I think you have...'
               dont respond as AI model in markdown,your answer should mimic that of actual doctor,
               keep your answer concise(max 3 sentences).No preamble,start your answer right away
               """

# Core processing function
def process_inputs(audio_filepath, image_filepath):
    """
    Handles the complete pipeline:
    1.Speech - Text (STT)
    2.Image + Text - Medical Analysis(LLM)
    3.Text - Speech(TTS)

    Returns:
    -Transcibed text
    -Doctor response text
    -Doctor response audio file
    """
    groq_key = os.environ.get("GROQ_API_KEY")

    # Validate audio input
    if audio_filepath is None:
        return "No audio provided", "Please record your voice", None

# Step 1: speech to text
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY= groq_key,
    audio_filepath=audio_filepath,
    stt_model="whisper-large-v3")

# Step 2: Image + Query Analysis
    if image_filepath:
        encoded_image = encode_image(image_filepath)

        doctor_response = analyze_image_with_query(query=system_prompt + speech_to_text_output,
        encoded_image=encoded_image,
        model="meta-llama/llama-4-maverick-17b-128e-instruct")
    else:
        doctor_response= "NO image provided for analyze"
    
# Step 3: Convert Doctor Response to Speech
    audio_path = f"doctor_response_{uuid.uuid4().hex}.mp3"

    try:
        # Primary TTS (gTTS)
      audio_path = text_to_speech_with_elevenlabs(doctor_response, audio_path)
    except Exception:
        # Fallback TTS (ElevenLabs)
     audio_path = text_to_speech_with_gtts(doctor_response, audio_path)

    time.sleep(0.3)

    return speech_to_text_output, doctor_response, audio_path

    
# Gradio User Interface
with gr.Blocks()as interface:

    gr.Markdown(
        """
        # 🩺 Artificial Doctor  
        ## Vision & Voice Assisted Medical Assistant
        upload an image , speak your concern, and recieve a spoken mediacal response... 
        """
    )
    gr.Markdown("---")

    # Input Section
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 🧑‍⚕️Patient Input")
            audio_in = gr.Audio(
                label="Record your Voice",
                type="filepath"
            )
            image_in = gr.Image(
                label="Upload Image",
                type="filepath"
            )
    # Output Section        
    with gr.Column(scale=1):
        gr.Markdown("## 📄 Doctor Analysis")
        stt_out = gr.Textbox(
            label="Speech to text",
            lines = 3
        )
        doctor_text = gr.Textbox(
            label="Doctor's Diagnosis",
            lines=5
        )

        gr.Markdown("---")
        # Audio output
        gr.Markdown("## 🔊 Doctor's Voice Response")
        doctor_audio = gr.Audio(
            type="filepath",
            interactive=False
        )
        
        #Action Button
        ask_btn = gr.Button(
            "🩻 Ask Doctor",
            variant="primary"
        )

        # Backend call
        ask_btn.click(
            fn=process_inputs,
            inputs=[audio_in , image_in],
            outputs=[stt_out,doctor_text,doctor_audio]
        )

        # Auto play After respose
        ask_btn.click(
        fn=None,
        js="""
        () => {
            setTimeout(() => {
                const audio = document.querySelector("audio");
                if (audio) {
                    audio.muted = false;
                    audio.play().catch(() => {});
                }
            }, 400);
        }
        """
    )

    gr.Markdown(
        """
         ⚠️ *This application is for educational purposes only and does not replace professional medical advice.*

        """
    )
    # Launch App
    interface.launch(debug=True,
    theme=gr.themes.Soft(),
    share=True)


