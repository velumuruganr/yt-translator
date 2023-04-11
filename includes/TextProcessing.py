import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import translators

AUDIO_PATH = 'static/downloaded-audio.wav'

class TextProcessing:
    def __init__(self) -> None:
        pass
    

    def to_text():
        r = sr.Recognizer()
        sound = AudioSegment.from_file(file=AUDIO_PATH, format='wav')
        chunks = split_on_silence(sound,
            min_silence_len = 500,
            silence_thresh = sound.dBFS-14,
            keep_silence=500,
        )
        folder_name = "static/audio-chunks"
        # create a directory to store the audio chunks
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        whole_text = ""
        
        print(f'Total Number of Chunks:{len(chunks)}')
        
        translators.preaccelerate()
        # process each chunk 
        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory.
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # recognize the chunk
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                # try converting it to text
                try:
                    text = r.recognize_google(audio_listened)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    translation = translators.translate_text(text, from_language="hi", to_language="en")
                    print(chunk_filename, ":", translation)
                    whole_text += translation
        # return the text for all chunks detected
        return whole_text

                        