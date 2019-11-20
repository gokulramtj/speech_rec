import speech_recognition as sr 
import time
from datetime import datetime
import multiprocessing


def recognize(audio):
    try: 
        text = r.recognize_google(audio) 
        print("you said: " + text)
        print("Writing to file...")
        f.write(text)
        flag = True


    except sr.UnknownValueError: 
        print("Could not understand audio") 
        flag = False

    except sr.RequestError as e: 
        print("Could not connect to internet {0}".format(e)) 
        flag = False
    return flag

mic_name = "Headset (MiSuperBassWirelessHea"
sample_rate = 48000
chunk_size = 2048
flag = True
r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names() 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        
        device_id = i 
        dname = str(datetime.fromtimestamp(time.time()))
        dname = dname.replace(" ", "_")
        dname = dname.replace(":", "-")
        name = "speech_to_text\\" + dname +".txt"
        print("\nCreating file : " + dname + ".txt")
        f = open(name ,"a+")
            

        while flag:
            
            with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                                chunk_size = chunk_size) as source: 
            
                r.adjust_for_ambient_noise(source) 
                print("Say Something")
                audio = r.listen(source) 
                print("Recognizing")
                try: 
                    text = r.recognize_google(audio) 
                    print("you said: " + text)

                    print("Writing to file...")
                    f.write(text)


                except sr.UnknownValueError: 
                    print("Could not understand audio") 
                    flag = False

                except sr.RequestError as e: 
                    print("Could not connect to internet {0}".format(e)) 
                    flag = False
        f.close()
        print("Write completed.\nRefer file : " + name)