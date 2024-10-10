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
    Model(1, "Small_model_ru", "..\Small_model_ru"),
    Model(2, "Big_model_ru", "..\Big_model_ru")
]

def param_setup():
    p = pyaudio.PyAudio()

    device_count = p.get_device_count()

    for i in range(device_count):
        device_info = p.get_device_info_by_index(i)

        if device_info['maxInputChannels'] != 0:
            print(f"Device {i}: {device_info['name']}, Input Channels: {device_info['maxInputChannels']}")

    mic_index = int(input("Enter mic number: "))


    for element in Models:
        print(element)

    try:
        user_index = int(input("\nEnter index: "))

        if 1 <= user_index <= len(Models):
            model = Models[user_index - 1]
            model_path = model.path
            print(f"\nUsing:\n{model}")
        else:
            print("Incorrect index, try again.")
            exit(401)

    except ValueError:
        print("Incorrect input.")
        exit(401)

    return mic_index, model_path
