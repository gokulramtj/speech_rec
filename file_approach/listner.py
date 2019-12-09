import speech_recognition as sr 
import time
from datetime import datetime
import pickle


mic_name = "Headset (MiSuperBassWirelessHea"
sample_rate = 48000
chunk_size = 2048
flag = True
r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names() 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i  
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                            chunk_size = chunk_size) as source: 
            while True:
                r.adjust_for_ambient_noise(source) 
                print("Say Something")
                audio = r.listen(source) 
                print("Recognizing")
                name = str(datetime.fromtimestamp(time.time()))
                name = name.replace(" ", "_")
                name = name.replace(":", "-")
                pickle_out = open("transcrpit_aud\\"+name+".flag", "wb")
                pickle.dump(0, pickle_out)
                pickle_out.close()
                pickle_out = open("transcrpit_aud\\"+name+".audio", "wb")
                pickle.dump(audio, pickle_out)
                pickle_out.close()
                pickle_out = open("transcrpit_aud\\"+name+".flag", "wb")
                pickle.dump(1, pickle_out)
                pickle_out.close()