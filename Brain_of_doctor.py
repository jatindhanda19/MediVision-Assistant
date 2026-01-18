"""
Brain of Doctor - Multimodel AI (Text + Image)

This script sends user query along with medical image to
multimodal LLM using Groq API and returns the AI analysis.

Use Case:
-AI medical Assistant
-Image based health query analysis

Requirements:
-groq
-python-dotenv
"""

# Step 1: Load Environment Variables (API Keys)
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Fetch API Key securely
GROQ_API_KEY= os.environ.get("GROQ_API_KEY")


# Step 2: Convert Image to Base64 (Required by API)
import base64

#image_path = "dandruff.jpg"

def encode_image(image_path):
    """
    Converts an image file into base64 format.
    
    Parameters:
    -image_path : path to image file
    
    Return:
    -str: Base64 encoded image
    """

    with open(image_path,"rb") as image_file:
       return base64.b64encode(image_file.read()).decode('utf-8')
      
#Step 3: Setup multimodal LLM (Text + Image)
from groq import Groq

# Example user question
query = "Is there something wrong with my face?"

# Multimodal LLM model
model = "meta-llama/llama-4-maverick-17b-128e-instruct"

def analyze_image_with_query(query,model,encoded_image):
    """
    Sends a user query and image to Groq's multimodal LLM
    and return the AI-generated response
    
    Parameters:
    -query: User question
    -model: LLM model name
    -encoded image : Base64 encoded image
    
    Returns:
    -str: AI response
    """ 

    # Intialize Groq client
    client = Groq(api_key=GROQ_API_KEY) 

    # Prepare muyltimodal input messages
    messages = [
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text": query
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
     
    # Call Groq chat completion API
    chat_completion=client.chat.completions.create(
        messages = messages,
        model = model
    )

    # Return AI response text
    return chat_completion.choices[0].message.content

