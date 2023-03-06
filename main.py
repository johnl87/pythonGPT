#importing openai library
import openai

API_KEY = '<>'
openai.api_key = API_KEY
model_name = 'cloneGPT-3.5'

def chatGPT(prompts):
    response = openai.ChatCompletion.create (
        model = model_name,
        messages = prompts
    )

    prompts.append({'type': response.choices[0].message.role,
                    'content': response.choices[0].message.content})
    return prompts

prompts = []
prompts.


