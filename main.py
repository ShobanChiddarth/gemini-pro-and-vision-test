import json
from pathlib import Path
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

with open("api_keys.json") as f:
    api_key = json.load(f)["Google-Generative-Language"]
    genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings,)

prompt = """\
Generate an ordered list of everything in this image. After generating the list,\
append two newlines to your response and give a yes or no response if there are any\
weapons (or anything else that could be used to harm someone or even commit any crime)\
in the image. If there are any such things, add two newlines to your response and list them.

Here is an example response for the image having no weapons:

```
1. A person
2. A dog
3. A tree
4. A car
5. A house

No
```

Here is an example response for the image having weapons:

```
1. A person
2. A gun
3. A knife
4. A tree
5. A car

Yes

1. A gun
2. A knife
```
"""

image_parts = [
  {
    "mime_type": "image/jpeg",
    "data": Path("image.jpg").read_bytes()
  },
]

prompt_parts = [prompt, image_parts[0]]

response = model.generate_content(prompt_parts)

print(response.text.strip())
