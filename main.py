from param_setup import param_setup
from speech_rec import decode

TRIG_WORD = ""

def main():
    (mic_index,
     model_path,
     time_until_off_vosk) \
        = param_setup()

    for text in decode(mic_index, model_path, time_until_off_vosk):
        print(text)
        if TRIG_WORD in text:
            pass


if __name__ == "__main__":
    main()

