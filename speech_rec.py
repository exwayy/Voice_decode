import pyaudio
from vosk import Model, KaldiRecognizer
import json
import time

sound = pyaudio.PyAudio()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 8000


def stream_init(mic_index):
    return sound.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=mic_index,
        frames_per_buffer=CHUNK
    )


def decode(mic_index, model_path, time_until_off_vosk):
    print("decode - READY")

    stream = stream_init(mic_index)
    model_ru = Model(model_path)
    rec_ru = KaldiRecognizer(model_ru, RATE)
    time_last_activity = time.time()

    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            if len(data) > 0:
                if rec_ru.AcceptWaveform(data):
                    time_last_activity = time.time()
                    answer_ru = json.loads(rec_ru.Result())
                    if answer_ru['text']:
                        yield answer_ru['text']
                else:
                    # Проверка на тишину
                    if time.time() - time_last_activity > time_until_off_vosk:
                        print("Cleaning cache.")
                        stream.stop_stream()
                        stream.close()
                        stream = stream_init(mic_index)
                        time_last_activity = time.time()

    except KeyboardInterrupt:
        print(523)

    finally:
        stream.stop_stream()
        stream.close()
        model_ru = None
        del model_ru
        print("Stream closed.")
