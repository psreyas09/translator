# Language Translator App

This is a simple GUI-based language translator application built using Python and Tkinter. It uses the Azure Translator API to translate text into different languages.

## Features
- Translate text into any supported language.
- Simple and user-friendly GUI using Tkinter.
- Uses Azure Translator API.

## Prerequisites
- Python 3.x installed.
- An active Azure Translator API key.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/translator-app.git
   cd translator-app

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows


3. Install required packages:

pip install -r requirements.txt

If requirements.txt is missing, manually install dependencies:

pip install requests tk


4. Replace "your_api_key_here" in translator.py with your own Azure Translator API key.


5. Run the script:

python translator.py



Dependencies

The project requires the following Python packages:

requests – For making API calls to Azure Translator.

tk (Tkinter) – For the GUI interface.


License

This project is licensed under the MIT License - see the LICENSE file for details.

Author

Sreyas P


---

### **requirements.txt**  
You should also create a `requirements.txt` file for easy package installation:

requests tk
