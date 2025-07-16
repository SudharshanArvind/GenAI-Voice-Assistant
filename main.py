import speech_recognition as sr
import whisper
import requests
from gtts import gTTS
from playsound import playsound
import tempfile
import os
import langdetect

# Load Whisper model (base/medium for better multilingual)
print("📦 Loading Whisper model...")
model = whisper.load_model("small")

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Speak your question in any language...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
        print("✅ Audio captured.")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        audio_path = f.name
        f.write(audio_data.get_wav_data())
    return audio_path

def transcribe_audio(audio_path):
    try:
        print("🧠 Transcribing...")
        result = model.transcribe(audio_path)
        os.remove(audio_path)
        print(f"🗣️ You asked: {result['text']}")
        return result['text']
    except Exception as e:
        print("❌ Transcription failed:", e)
        return None

def detect_language(text):
    try:
        from langdetect import detect
        lang_code = detect(text)
        print(f"🌐 Detected Language: {lang_code}")
        return lang_code
    except Exception as e:
        print("❌ Language detection failed:", e)
        return 'en'

def ask_gemma(prompt):
    print("🤖 Gemma is thinking...")
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma3:12b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            reply = response.json()["response"]
            print(f"💬 Gemma says: {reply}")
            return reply
        else:
            print("❌ Ollama error:", response.text)
            return "Sorry, I couldn't process your request."
    except Exception as e:
        print("❌ Error contacting Ollama:", e)
        return "Gemma failed to respond."

def speak_text(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            temp_audio = f.name
            tts.save(temp_audio)
        playsound(temp_audio)
        os.remove(temp_audio)
    except Exception as e:
        print("❌ TTS error:", e)

# 🔁 Main Loop
while True:
    try:
        audio_file = record_audio()
        user_text = transcribe_audio(audio_file)

        if not user_text:
            print("⚠️ No input detected.")
            continue

        if user_text.lower() in ["exit", "quit", "stop"]:
            speak_text("Goodbye!", 'en')
            break

        lang_code = detect_language(user_text)
        gemma_reply = ask_gemma(user_text)
        speak_text(gemma_reply, lang=lang_code)

    except KeyboardInterrupt:
        print("🛑 Interrupted by user.")
        break