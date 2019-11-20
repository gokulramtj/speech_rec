import speech_recognition as sr 
import time
from datetime import datetime

mic_name = "Microsoft Sound Mapper - Input"
sample_rate = 16000
chunk_size = 2048
r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names() 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 
        dname = str(datetime.fromtimestamp(time.time()))
        dname = dname.replace(" ", "_")
        dname = dname.replace(":", "-")
        name = "speech_to_text\\" + dname +".txt"
        print("\nCreating file at: " + name)
        print("Start Speaking")
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                                chunk_size = chunk_size) as source: 
        	while True:
	            r.adjust_for_ambient_noise(source)
	            audio = r.listen(source) 
	            text = r.recognize_sphinx(audio)
	            print("you said: " + text)
	            f = open(name ,"a+")
	            print("Writing to file...")
	            f.write(text)
	            f.close()
	            