# 🗣️ Multilingual Voice Assistant using Whisper and Gemma

This project is an AI-powered **Multilingual Voice Assistant** built with Python. It captures spoken input in any language, transcribes it using OpenAI's Whisper model, detects the spoken language, sends the query to **Gemma (via Ollama)** for an intelligent response, and finally speaks the answer back using Google's TTS.

## 🚀 Features

- 🎤 Real-time voice capture
- 🧠 Whisper-based multilingual transcription
- 🌍 Language detection via `langdetect`
- 🤖 AI responses from local **Gemma model** through Ollama API
- 🔊 Speech output using `gTTS` and `playsound`
- 🔁 Continuous conversation loop with `exit`, `stop`, or `quit` commands

## 🧰 Tech Stack

| Component     | Tech Used              |
|---------------|------------------------|
| Transcription | [Whisper](https://github.com/openai/whisper) |
| Voice Input   | [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) |
| AI Response   | [Gemma via Ollama API](https://ollama.com/) |
| Language Detection | [langdetect](https://pypi.org/project/langdetect/) |
| Text-to-Speech | [gTTS](https://pypi.org/project/gTTS/), [playsound](https://pypi.org/project/playsound/) |
| Deployment    | Localhost (can be containerized or deployed using Netlify + Supabase for advanced features) |

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Ollama and Gemma model installed locally
- `ffmpeg` (required by Whisper)

### Setup Instructions

```bash
# 1. Clone this repository
git clone https://github.com/your-username/voice-gemma-assistant.git
cd voice-gemma-assistant

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## 🧠 Ollama & Gemma Setup (LLM Backend)

### Step-by-Step Setup

1. Install Ollama (if not already installed)

  - Download from: https://ollama.com/download

  - Follow OS-specific installation instructions.

2. Pull the Gemma Model
```
ollama pull gemma3:12b
```
This will download and prepare the 12B Gemma model locally.

3. Start Ollama Server
Make sure the Ollama backend is running:
```
ollama run gemma3:12b
```
This will serve Gemma locally at http://localhost:11434, which the Python script uses to fetch responses.


## 🧪 Running the Assistant
```
python app.py
```
### Usage Tips:

- Speak in any language.

- Say "exit", "quit", or "stop" to terminate the loop.

- Ensure you're connected to the internet (for gTTS).

- Ensure Ollama is running before launching the script.

## 📌 requirements.txt

- speechrecognition
- whisper
- gtts
- playsound
- langdetect
- requests

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
