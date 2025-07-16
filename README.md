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
