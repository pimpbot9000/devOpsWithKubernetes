from flask import Flask, jsonify, request, Response, abort
import time
import sys

# global counter
count_this = 0

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    
    response_str = 'pong {counter}'.format(counter=count_this)   
    
    increment()

    return Response(response_str, status=200)

def increment():
    global count_this 
    count_this = count_this + 1  

if __name__ == "__main__":

    from waitress import serve

    port = 3000
    
    try:
        port = sys.argv[1:][0]
    except:
        pass    
    
    host = "0.0.0.0"    
    print('Bong server started in port {port}'.format(port=port))    
    serve(app, host=host, port=port)
