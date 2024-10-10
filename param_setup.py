import pyaudio


class Model:
    def __init__(self, index, name, path):
        self.index = index
        self.name = name
        self.path = path

    def __str__(self):
        return f"Index: {self.index}, Name: {self.name}, Path: {self.path}"

# Список моделей


Models = [
    Model(1, "Small_model_ru", "..\\Small_model_ru"),
    Model(2, "Big_model_ru", "..\\Big_model_ru")
]


def param_setup():

    p = pyaudio.PyAudio()

    device_count = p.get_device_count()
    print("Available devices:")

    for i in range(device_count):

        device_info = p.get_device_info_by_index(i)

        if device_info['maxInputChannels'] != 0:

            print(f"Device {i}: {device_info['name']}, Input Channels: {device_info['maxInputChannels']}")

    try:

        mic_index = int(input("\n"+"Enter mic number: "))

        if not 1 <= mic_index <= device_count:

            print("Not found.")
            exit(404)

        device_info=p.get_device_info_by_index(mic_index)
        print("\n"+f"Using device: {mic_index}: {device_info['name']}, Input Channels: {device_info['maxInputChannels']}"+"\n")
        for element in Models:
            print(element)


        user_index = int(input("\nEnter index: "))

        if 1 <= user_index <= len(Models):

            model = Models[user_index - 1]
            model_path = model.path
            print(f"\nUsing \n{user_index}: {model.name}, {model.path}")

        else:

            print("Not found.")
            exit(404)

    except ValueError:
        print("Incorrect input.")
        exit(400)

    print("\n")

    time_until_off_vosk=int(input("Time threshold until off speech recognition(sec): "))

    return mic_index, model_path, time_until_off_vosk
