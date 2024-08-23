import streamlit as st
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

def get_default_audio_device():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))

def get_current_volume():
    volume = get_default_audio_device()
    current_volume = volume.GetMasterVolumeLevelScalar()
    return int(current_volume * 100)

def set_volume(level):
    volume = get_default_audio_device()
    if 0 <= level <= 100:
        volume.SetMasterVolumeLevelScalar(level / 100, None)
        st.success(f"Volume set to {level}%")
    else:
        st.warning("Volume level must be between 0 and 100")

st.title("Audio Volume Control")
st.write("Adjust the volume of your default audio device.")

current_volume = get_current_volume()
st.write(f"Current volume: {current_volume}%")

new_volume = st.slider("Set new volume level (0-100)", min_value=0, max_value=100, value=current_volume)

if st.button("Set Volume"):
    set_volume(new_volume)

