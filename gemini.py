# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login

import vertexai
from vertexai.generative_models import GenerativeModel, Part


model = GenerativeModel('gemini-pro')

def eng_to_ASL(english_sentence):
    prompt = f"""
translate the given english sentence into an English sentence that is structured according to the American Sign Language grammar. 

Few shot Examples:
```English: "I am going to the store."```
```ASL Structure: "STORE I GO"```

```English: "What is your name?"```
```ASL Structure: "YOUR NAME WHAT"```

```English: "Do you want to eat pizza or spaghetti?"```
```ASL Structure: "PIZZA SPAGHETTI WHICH YOU WANT EAT"```

Reply ONLY with the answer that goes into <YOUR_ANSWER> below. ONLY with the answer.:
```Enlgish: "{english_sentence}"```
```ASL: 

<YOUR_ANSWER>```
"""
    response = model.generate_content(prompt)
    print(response.text) #  The opposite of hot is cold.

eng_to_ASL('I love your wife')