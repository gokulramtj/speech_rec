# importing the requests library 
import subprocess as sp
import speech_recognition as sr 
import time
from datetime import datetime
import multiprocessing
import requests
import pickle

global str

URL = "http://localhost:8000"
sp.call('cls', shell=True)
print('\n\n\n---------------------------------------------------------------------------------------')
print('Speech Rec')
print('---------------------------------------------------------------------------------------\n\n\n')

# mic_name = "Headphones ()"
mic_name = "Headset (MiSuperBassWirelessHea"
sample_rate = 48000
chunk_size = 2048
flag = True
r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names() 
for i, microphone_name in enumerate(mic_list): 
    print(microphone_name)
    if microphone_name == mic_name: 
        device_id = i 
        while flag:
            with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                                chunk_size = chunk_size) as source: 
                r.adjust_for_ambient_noise(source) 
                while True:
                    print("Say Something")
                    audio = r.listen(source) 
                    print("Recorded")
                    name = str(datetime.fromtimestamp(time.time()))
                    name = name.replace(" ", "_")
                    name = name.replace(":", "-")
                    pickle_out = open(name, "wb")
                    pickle.dump(audio, pickle_out)
                    pickle_out.close()
                    parameters = {'Audio': name}
                    # text = r.recognize_google(pickle.load(pickle_in)) 
                    requests.post(url=URL, json=parameters)
                    # sp.call('cls', shell=True)
                
