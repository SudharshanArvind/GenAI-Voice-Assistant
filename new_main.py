import speech_recognition as sr
import whisper
import google.generativeai as genai
import tempfile
import os
from gtts import gTTS
from playsound import playsound
from langdetect import detect

# 📌 Insert your Gemini API Key here (or use env var)
GOOGLE_API_KEY = "YOUR_API_KEY"

# Authenticate with Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Whisper model
print("📦 Loading Whisper model...")
model = whisper.load_model("small")

# 🎙️ Record user's voice
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

# 🧠 Transcribe voice to text
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

# 🌍 Detect language from text
def detect_language(text):
    try:
        lang_code = detect(text)
        print(f"🌐 Detected Language: {lang_code}")
        return lang_code
    except Exception as e:
        print("❌ Language detection failed:", e)
        return 'en'

# 🤖 Ask Gemini AI for response
def ask_gemini(prompt):
    print("🤖 Gemini is thinking...")
    try:
        model = genai.GenerativeModel(model_name="models/gemini-pro")
        response = model.generate_content(prompt)
        reply = response.text
        print(f"💬 Gemini says: {reply}")
        return reply
    except Exception as e:
        print("❌ Gemini API error:", e)
        return "Sorry, I couldn't process your request."


# 🔊 Speak the AI response
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

# 🔁 Main loop
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
        gemini_reply = ask_gemini(user_text)
        speak_text(gemini_reply, lang=lang_code)

    except KeyboardInterrupt:
        print("🛑 Interrupted by user.")
        break
