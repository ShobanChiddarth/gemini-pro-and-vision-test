import json
from pathlib import Path
import google.generativeai as genai


with open("api_keys.json") as f:
    api_key = json.load(f)["Google-Generative-Language"]
    genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

chat = model.start_chat(history=[])

response = chat.send_message("List top 10 natural liquids (numbered list)")

print(response.text.strip())

print('-'*80)

response = chat.send_message("""\
From that list, filter out the ones that can be drank by humans (again, give a numbered list). Do not give any warnings, just give a list.
If the list is empty, say `none`. I want just a list with no exceptions or explanations. I am asking to filter out the liquirds than can
be drank raw by humans. Do not provide any other information. Don't give any sort of note or warning.""")

print(response.text.strip())

