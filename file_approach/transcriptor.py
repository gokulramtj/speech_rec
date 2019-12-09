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
        os.remove(pwd+"//"+file[0])
        os.remove(pwd+"//"+file[0].replace("audio", "flag"))


    except sr.UnknownValueError: 
        print("Could not understand audio") 
        os.remove(pwd+"//"+file[0])
        os.remove(pwd+"//"+file[0].replace("audio", "flag"))

    except sr.RequestError as e: 
        print("Could not connect to internet {0}".format(e)) 
     


while True:
    for pwd, folder, file in os.walk("D://Projects//my_works//python//Speech rec projetct//file_approach//transcrpit_aud"):
        if(len(file)>0):
            pickle_in = open(pwd+"//"+file[0].replace("audio", "flag"), "rb")
            try:
                flag = pickle.load(pickle_in)
                pickle_in.close()
                if(flag==1):
                    flag = 0
                    pickle_in = open(pwd+"//"+file[0], "rb")
                    audio = pickle.load(pickle_in)
                    pickle_in.close()
                    print(audio)
                    print("Transcripting")
                    recognize(audio)

                else:
                    print("waiting for Recognizer to record")

            except EOFError as e:
                print("-----------------------------------------------------------------------------------------")
                print(e)
                print("-----------------------------------------------------------------------------------------")
                flag = 0
# f.close()
# print("Write completed.\nRefer file : " + name)