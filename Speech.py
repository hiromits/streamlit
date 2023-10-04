!pip install streamlit SpeechRecognition
import streamlit as st
import speech_recognition as sr

st.title('音声認識アプリ')

uploaded_file = st.file_uploader("音声ファイルをアップロードしてください。", type=["wav", "flac"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/wav')
    
    # 音声認識のオブジェクト作成
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(uploaded_file)
    
    # 音声ファイルをテキストに変換
    with audio_file as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio, language='ja-JP')
        st.write("認識結果:")
        st.write(text)
    except sr.UnknownValueError:
        st.write("音声を認識できませんでした。")
    except sr.RequestError as e:
        st.write(f"音声認識サービスからエラーが返されました; {e}")
