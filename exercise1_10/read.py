from flask import Flask, jsonify, request, Response, abort
import hashlib
import time
import sys

# global hash
hs = ""
app = Flask(__name__)
filename = ""

@app.route('/', methods=['GET'])
def root():
    #arg = request.args.get('name')
    f = open(filename, "r")
    timestamp = f.readline() #contains the
    f.close()    
    
    response_str = 'Application {hs}. Read timestamp {timestamp}'.format(hs=hs, timestamp=timestamp)
    return Response(response_str, status=200)
   

if __name__ == "__main__":
    from waitress import serve

    port = 8080     
    
    try:
        filename = sys.argv[1:][0]
        print("filename:", filename)
    except:
        print("filename missing. exit.")
        exit()
    
    host = "0.0.0.0"    
    hs = hashlib.sha256(str(time.time()).encode('utf-8')).hexdigest()[0:10]
    print('Server started in port {port}'.format(port=port))    
    serve(app, host=host, port=port)