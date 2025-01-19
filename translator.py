import requests
from tkinter import Tk, Label, Button, Entry, Text, END

# Azure Translator API Details
subscription_key = "FxCZCqMMafdlOCvYv4qTiA6SJn8GzusFNF27bQpTJ6gjBz56VslPJQQJ99BAACGhslBXJ3w3AAAbACOGD9vw"  # Replace with your Azure API key
endpoint = "https://api.cognitive.microsofttranslator.com/"  # Replace with your endpoint
location = "global"  # Set to your Azure region

def translate_text():
    # Get user input
    text_to_translate = input_text.get("1.0", END).strip()
    target_language = lang_entry.get().strip()
    
    # Validate input
    if not text_to_translate or not target_language:
        result_label.config(text="Please enter text and target language.")
        return
    
    # API request
    path = '/translate'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-Type': 'application/json'
    }
    body = [{
        'text': text_to_translate
    }]
    params = {
        'api-version': '3.0',
        'to': target_language
    }

    response = requests.post(constructed_url, headers=headers, params=params, json=body)
    if response.status_code == 200:
        result = response.json()
        translation = result[0]['translations'][0]['text']
        result_label.config(text=f"Translation: {translation}")
    else:
        result_label.config(text="Error: Unable to translate.")

# GUI Setup
app = Tk()
app.title("Language Translator")

Label(app, text="Enter text to translate:").grid(row=0, column=0, padx=10, pady=10)
input_text = Text(app, height=5, width=50)
input_text.grid(row=1, column=0, padx=10, pady=10)

Label(app, text="Target language (e.g., 'es' for Spanish):").grid(row=2, column=0, padx=10, pady=10)
lang_entry = Entry(app)
lang_entry.grid(row=3, column=0, padx=10, pady=10)

translate_button = Button(app, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, padx=10, pady=10)

result_label = Label(app, text="", wraplength=400)
result_label.grid(row=5, column=0, padx=10, pady=10)

app.mainloop()
