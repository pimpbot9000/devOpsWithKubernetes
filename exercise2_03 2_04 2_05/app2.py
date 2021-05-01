from flask import Flask, jsonify, request, Response, abort, render_template
import hashlib
import time
import sys
import requests
import os
import json

# global hash
hs = ""
timestamp_filename = ""
image_filename = ""
path = ""
app = Flask(__name__)
pong_url = ""
counter_url = ""
message = ""

@app.route('/health')
def health():
    print("Health check!")
    return "I'm healthy"

@app.route('/', methods=['GET'])
def root():

    response_hash = create_hash(str(time.time()))
    counter = read_counter()
    timestamp = read_timestamp()

    if timestamp + 24*60*60 < time.time():
        download_image(image_filename)
        write_timestamp()

    todos = json.loads(get_todos())
    print(todos)
    return render_template("index.html", message=message, hs=hs, response_hash=response_hash, counter=counter, timestamp=timestamp, todos=todos)

def get_todos():    
    result = requests.get("http://backend-service-internal/todos").content.decode("utf-8")
    print(result)
    return result

def read_counter():
    try:        
        return requests.get(counter_url).content.decode("utf-8") 
    except:
        return 0

def read_timestamp():
    try:
        f = open(timestamp_filename, "r")
        timestamp = f.read()
        f.close()
        return int(float(timestamp))
    except:
        return 0

def write_timestamp():
    f = open(timestamp_filename, "w")
    f.write(str(time.time()))
    f.close()

def create_hash(seed_str):
    return hashlib.sha256(seed_str.encode('utf-8')).hexdigest()[0:10]

def download_image(filename):
    response = requests.get("https://picsum.photos/1200")
    file = open(filename, "wb")
    file.write(response.content)
    file.close()


if __name__ == "__main__":
    from waitress import serve

    port = 7070
    args = sys.argv[1:]
    print(args)
    # args: path pong-url
    try:
        path = args[0]        
        counter_url = args[1]
        filename = os.path.join(path, "file.txt")
        image_filename = os.path.join(path, "image.jpg")
        timestamp_filename = os.path.join(path, "timestamp.txt")
        
        print("filename:", filename)
        print("image filename", image_filename)
        print("timestamp filename", timestamp_filename)
        print("path:", path)
        download_image(image_filename)
        write_timestamp()        

    except:        
        print("No path")
        exit()

   

    host = "0.0.0.0"    
    hs = create_hash(str(time.time()))
    print('my-secret:', os.getenv('MY_SECRET'))
    message = os.getenv('MESSAGE')
    print(message)
    print('Server started in port {port}'.format(port=port))    
    serve(app, host=host, port=port)
    