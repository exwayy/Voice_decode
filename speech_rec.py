import pyaudio
from vosk import Model, KaldiRecognizer
import json

sound = pyaudio.PyAudio()



def decode(mic_index,model_path):
    model_ru = Model(model_path)
    rec_ru = KaldiRecognizer(model_ru, 16000)

    print("decode - READY")
    stream = sound.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        input_device_index=mic_index,
        frames_per_buffer=8000
    )

    stream.start_stream()

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec_ru.AcceptWaveform(data)  and len(data) > 0:
            answer_ru = json.loads(rec_ru.Result())
            if answer_ru['text']:
                yield answer_ru['text']


