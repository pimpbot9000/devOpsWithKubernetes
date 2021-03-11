from flask import Flask, jsonify, request, Response, abort
import hashlib
import time
import sys

# global hash
hs = ""
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    #arg = request.args.get('name')
    response_hash = hashlib.sha256(str(time.time()).encode('utf-8')).hexdigest()[0:10]
    
    response_str = 'Application {hs}. Response {response_hash}'.format(hs=hs, response_hash=response_hash)

    return Response(response_str, status=200)
   

if __name__ == "__main__":
    from waitress import serve

    port = 8080

    try:
        port = sys.argv[1:][0]
    except:
        pass
    
    host = "0.0.0.0"    
    hs = hashlib.sha256(str(time.time()).encode('utf-8')).hexdigest()[0:10]
    print('Server started in port {port}'.format(port=port))    
    serve(app, host=host, port=port)
    