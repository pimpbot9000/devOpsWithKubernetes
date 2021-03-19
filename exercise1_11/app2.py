from flask import Flask, jsonify, request, Response, abort
import hashlib
import time
import sys

# global hash
hs = ""
filename = ""
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    
    response_hash = create_hash(str(time.time()))
    counter = read()
    response_str = 'Application {hs}. Response {response_hash}.\nPing/pong: {counter}'.format(hs=hs, response_hash=response_hash, counter=counter)

    return Response(response_str, status=200)

def read():
    try:
        f = open(filename, "r")
        count = f.read()
        f.close()
        return count
    except:
        return 0

def create_hash(seed_str):
    return hashlib.sha256(seed_str.encode('utf-8')).hexdigest()[0:10]

if __name__ == "__main__":
    from waitress import serve

    port = 8080

    try:
        filename = sys.argv[1:][0]
    except:
        print("Filename not found. Exiting")
        exit()

    host = "0.0.0.0"    
    hs = create_hash(str(time.time()))
    print('Server started in port {port}'.format(port=port))    
    serve(app, host=host, port=port)
    