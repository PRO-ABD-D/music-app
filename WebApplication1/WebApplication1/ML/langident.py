from lingua import Language, LanguageDetectorBuilder
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import wave

# def transcribe_offline(audio_path):
#     model = Model("path_to_vosk_model")  
#     wf = wave.open(audio_path, "rb")
#
#     if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000]:
#         raise ValueError("Audio file must be WAV format mono PCM with 8k or 16k sampling rate")
#
#     recognizer = KaldiRecognizer(model, wf.getframerate())
#     while True:
#         data = wf.readframes(4000)
#         if len(data) == 0:
#             break
#         if recognizer.AcceptWaveform(data):
#             print(recognizer.Result())
#     print(recognizer.FinalResult())
#
# transcribe_offline("output_file.wav")
#
# def transcribe_audio(audio_path):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_path) as source:
#         audio_data = recognizer.record(source)
#         try:
#             text = recognizer.recognize_google(audio_data) 
#             return text
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError:
#             print("API unavailable")
#     return None

detector = (
    LanguageDetectorBuilder
    .from_all_languages()
    .with_preloaded_language_models()
    .build()
)

text = "你好，世界！"

if text is not None:
    result = detector.detect_language_of(text)
    print(f"Detected language: {result.name}")  
else:
    print("No transcription available to detect the language.")
