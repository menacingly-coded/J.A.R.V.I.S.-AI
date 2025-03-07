# J.A.R.V.I.S.-AI

Jarvis AI is a Python-based virtual assistant that can process voice commands, respond using AI-generated text, and provide text-to-speech output. This project integrates Gemini AI API for intelligent responses and utilizes speech recognition and text-to-speech technologies.

## Features
- **Voice Recognition**: Converts spoken input into text using `speech_recognition`.
- **AI Chatbot**: Uses geminiAI's `ChatCompletion` to generate intelligent responses.
- **Text-to-Speech (TTS)**: Converts AI-generated responses into speech using `pyttsx3`.
- **Custom Commands**: Can be extended with custom functionalities like weather updates, web searches, or task automation.

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.7+ recommended). You can download it from [Python.org](https://www.python.org/downloads/).

### Clone the Repository
```bash
git clone https://github.com/yourusername/JarvisAI.git
cd JarvisAI
```

### Install Dependencies
Run the following command to install required libraries:
```bash
pip install -r requirements.txt
```

### Required API Keys
- **GeminiAI API Key**: Get your API key from geminiai api
- Store the API key in an environment variable or directly in the script:
  ```python
  import google.generativeai
  genai.configure = "your-api-key-here"
  ```

## Usage
Run the script:
```bash
python main.py
```
### How It Works
1. The assistant listens for voice input.
2. The voice input is converted into text.
3. The text is processed by GeminiAI's model to generate a response.
4. The response is spoken aloud using a text-to-speech engine.

## Troubleshooting
- **'say' is not recognized as a command**: Use `pyttsx3` instead of `say` for Windows.
- **GeminiAI API error**: Ensure you are using the correct GeminiAI API format (`ChatCompletion.create()` for newer versions).
- **Microphone issues**: Ensure your microphone is working and set as the default input device.

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit: `git commit -m "Add new feature"`
4. Push the branch: `git push origin feature-branch`
5. Create a Pull Request.

## Contact
For any questions or suggestions, feel free to open an issue or contact me at [shreya0987.edu@gmail.com](mailto:shreya0987.edu@gmail.com).

