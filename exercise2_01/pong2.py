from flask import Flask, jsonify, request, Response, abort
import time
import sys

#
#   Pong app for exercise 1.11
#   Reads and writes nof requests made into a file
#

filename = "file.txt"

app = Flask(__name__)

@app.route('/counter', methods=['GET'])
def get_count():
    counter = read()
    return Response(str(counter), status=200)

@app.route('/', methods=['GET'])
def root():

    counter = read()
    counter = int(counter) + 1
    response_str = 'I have been ponged {counter} times!'.format(counter=counter)   
    
    write(str(counter))

    return Response(response_str, status=200)

def write(count):
    f = open(filename, "w")
    f.write(count)
    f.close()
    
def read():
    f = open(filename, "r")
    count = f.read()
    f.close()
    return count

if __name__ == "__main__":

    from waitress import serve

    port = 6060   

    try:
        filename = sys.argv[1:][0]
    except:
        print("Filename not found. Exiting")  
    
    print("write to file: 0 ")
    write("0")

    host = "0.0.0.0"    
    print('Pong server started in port {port}'.format(port=port))    
    serve(app, host=host, port=port)