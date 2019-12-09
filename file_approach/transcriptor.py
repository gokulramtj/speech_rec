import speech_recognition as sr 
import time
from datetime import datetime
import os
import pickle

r = sr.Recognizer() 


dname = str(datetime.fromtimestamp(time.time()))
dname = dname.replace(" ", "_")
dname = dname.replace(":", "-")
name = "transcrpit_doc\\" + dname +".txt"
print("\nCreating file : " + dname + ".txt")


def recognize(audio):
    try: 
        text = r.recognize_google(audio) 
        print("you said: " + text)
        print("Writing to file...")
        f = open(name ,"a+")    
        f.write(text+" ")
        f.close()


    except sr.UnknownValueError: 
        print("Could not understand audio") 
        flag = True

    except sr.RequestError as e: 
        print("Could not connect to internet {0}".format(e)) 
        flag = False
     


while True:
    for pwd, folder, file in os.walk("D://Projects//my_works//python//Speech rec projetct//file_approach//transcrpit_aud"):
        if(len(file)>0):
            print(os.path.getsize(pwd+"//"+file[0]))
            pickle_in = open(pwd+"//"+file[0], "rb")
            audio = pickle.load(pickle_in)
            pickle_in.close()
            print("Transcripting")
            recognize(audio)

            os.remove(pwd+"//"+file[0])

# f.close()
# print("Write completed.\nRefer file : " + name)