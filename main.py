#importing openai library
import openai
import config

openai.api_key = config.API_KEY
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
prompts.append({'type': 'system', 'content': 'hi there'})
prompts = chatGPT(prompts)
print('{0}: {1}\n'.format(prompts[-1]['type'].strip(),prompts[-1]['content'].strip()))

while True:
    userPrompt = input('user:')
    prompts.append({'type': 'user', 'content': userPrompt})
    prompts = chatGPT(prompts)
    print('{0}: {1}\n'.format(prompts[-1]['type'].strip(),prompts[-1]['content'].strip()))


