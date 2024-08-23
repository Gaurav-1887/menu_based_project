import streamlit as st
from gtts import gTTS
import os

def text_to_audio(text, language='en'):
    try:
        speech = gTTS(text=text, lang=language, slow=False)

        audio_file = "output.mp3"
        speech.save(audio_file)
        return audio_file
    except Exception as e:
        st.error(f"Error occurred: {e}")
        return None

st.title("Text-to-Audio Converter")
st.write("Enter text below and click 'Convert to Audio' to generate an audio file.")

text_to_convert = st.text_area("Enter text:", height=150)


if st.button("Convert to Audio"):
    if text_to_convert.strip() == "":
        st.warning("Please enter some text to convert.")
    else:
        audio_file = text_to_audio(text_to_convert)
        if audio_file:
            st.success("Text converted successfully!")
            st.audio(audio_file, format='audio/mp3', start_time=0)
            st.markdown(f"### [Download Audio]({audio_file})")
        else:
            st.error("Failed to convert text to audio.")

