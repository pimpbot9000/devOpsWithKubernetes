from flask import Flask, jsonify, request, Response, abort, redirect
import sys
import json


todos = ["hello", "world"]
app = Flask(__name__)

@app.route('/todos', methods=['GET', 'POST'])
def get_todos():
    if request.method == 'GET':        
        return jsonify(todos)

    elif request.method == 'POST':
        data = request.get_json(force=True) #maybe there's a simpler way?
        todos.append(data['todo'])
        print("Just data", request.data)
        return Response("Ok", status=200)
    else:
        return Response("Not ok!", status=404)
        

if __name__ == "__main__":
    from waitress import serve

    port = 7070

    try:
        port = sys.argv[1:][0]
    except:
        pass
    
    host = "0.0.0.0" 
    print("In-memory backend at port", port)   
    serve(app, host=host, port=port)
    