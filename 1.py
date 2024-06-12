import streamlit as st
import speech_recognition as sr
def principal():
    st.title("Transição do audio: ")
    upload = st.file_uploader("Faça upload do arquivo de audio", type=["wav"[)
    if upload is not None:
        trasncrever(upload)


def transcrever(upload):
    recgnizer = sr.Recgnizer()
    with sr.AudioFile(upload) as source:
        st.write("Processando...")
        audio = recognizer.record(source)
        texto = recognizer.recognize_google(audio,language="pt-BR")
        st.write("Texto: ",texto)
principal()
                                                                       
