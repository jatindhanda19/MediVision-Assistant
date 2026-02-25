# 🩺 Multimodal LLM Medical Assistant (Voice + Vision AI)

## 📌 Project Overview

This project is a **Multimodal AI Medical Assistant** that can understand both **voice and image inputs** from a user and respond with a **medical-style analysis in text and audio format**.

The system simulates a simple **doctor–patient interaction**:

1. The patient **speaks their medical concern**
2. The patient **uploads an image** (face, skin, eye, etc.)
3. The AI analyzes the **speech + image**
4. The AI generates a **doctor-like response**
5. The response is returned as **text and spoken audio**

This project demonstrates how **Multimodal Large Language Models (LLMs)** can be used to build intelligent healthcare-style assistants.

⚠️ This project is **for educational purposes only** and does **not replace professional medical advice**.

---

# 🚀 Features
- Multimodal AI (Voice + Image input)
- Speech-to-Text using **Groq Whisper API**
- Image + Query analysis using **LLaMA multimodal model**
- Doctor-style response generation
- Text-to-Speech output (Doctor voice reply)
- Interactive UI using **Gradio**
- High-quality voice generation with **ElevenLabs**
- Fallback voice generation using **Google TTS**

---

# 🧠 System Workflow
Patient Voice → Speech to Text  
Patient Image + Query → Multimodal LLM  
LLM Response → Text  
Text → Speech  
Final Output → Doctor Voice Response

---

# 📂 Project Structure
multimodal-medical-assistant
│
├── app.py
├── Brain_of_doctor.py
├── voice_of_patient.py
├── voice_of_doctor.py
├── requirements.txt
├── .env
└── README.md
---

# 📄 File Description

### app.py
Main application file that runs the **Gradio interface** and connects all components together.

### Brain_of_doctor.py
Handles the **AI reasoning part**:
- Converts image to Base64
- Sends query + image to multimodal LLM
- Returns AI analysis

### voice_of_patient.py
Handles **patient voice input**:
- Records microphone audio
- Converts speech to text using Whisper

### voice_of_doctor.py
Handles **AI voice response**:
- Converts text response into speech
- Uses ElevenLabs for high quality voice
- Uses Google TTS as fallback

# 🛠 Technologies Used
Python  
Groq API  
Whisper Large V3  
LLaMA Multimodal Model  
Gradio  
ElevenLabs  
gTTS  
SpeechRecognition  
Pydub

## 🛠 Technologies Used
Python
Groq API
Whisper Large V3
LLaMA Multimodal Model
Gradio
ElevenLabs
gTTS
SpeechRecognition

## ⚠️ Disclaimer
This project is for educational purposes only and does not replace professional medical advice.

## 👨‍💻 Author
Jatin Dhanda
AI / Machine Learning Enthusiast
