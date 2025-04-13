from groq import Groq
from pathlib import Path
import base64
import streamlit as st

def generate_and_play_audio(text: str, voice: str = "Aaliyah-PlayAI"):
    """
    Generate speech from text using Groq TTS and play it via Streamlit.

    Args:
        text (str): Text to synthesize.
        voice (str): Voice model name (default: Aaliyah-PlayAI).
    """
    speech_file_path = Path("speech.wav")

    client = Groq()
    response = client.audio.speech.create(
        model="playai-tts",
        voice=voice,
        response_format="wav",
        input=text,
    )

    # Save audio output
    with open(speech_file_path, "wb") as f:
        f.write(response.read())

    # Embed and play in Streamlit
    with open(speech_file_path, "rb") as f:
        b64_audio = base64.b64encode(f.read()).decode()
        audio_html = f"""
        <audio autoplay>
            <source src="data:audio/wav;base64,{b64_audio}" type="audio/wav">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
