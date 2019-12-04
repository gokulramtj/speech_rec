import speech_recognition as sr 
import time
from datetime import datetime
import multiprocessing
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json
import subprocess as sp
import pickle
import os



r = sr.Recognizer() 
def recognize(parse):
    
    print(parse['Audio'])
    pickle_in = open(parse['Audio'], "rb")
    audio = pickle.load(pickle_in)
    pickle_in.close()


    try: 

        text = r.recognize_google(audio) 
        print("you said: " + text)

    except sr.UnknownValueError: 
        print("Could not understand audio") 

    except sr.RequestError as e: 
        print("Could not connect to internet {0}".format(e)) 

    os.remove(parse['Audio'])

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        print("get request called")

    def do_POST(self):
        # sp.call('cls', shell=True)
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.end_headers()
        # response = BytesIO()
        # response.write(b'This is POST request. ')
        # response.write(b'Received: ')
        # response.write(body)

        print("post request called")
        parse = json.loads(body.decode("utf-8"))
        recognize(parse)

print('hello')
       
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()