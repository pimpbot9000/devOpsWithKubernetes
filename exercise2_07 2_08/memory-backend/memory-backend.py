from flask import Flask, jsonify, request, Response
import sys
import json
from app import app
from app import db
from models import Todo


@app.route('/todos', methods=['GET', 'POST'])
def get_todos():
    if request.method == 'GET':
        todos = fetch_todos()
        return jsonify(todos)

    elif request.method == 'POST':
        data = request.get_json(force=True) # maybe there's a simpler way?
        save_todo(data['todo'])        
        return Response("Ok", status=200)
    else:
        return Response("Method not permitted.", status=404)

def fetch_todos():
    todos = [instance.todo for instance in db.session.query(Todo)]
    return todos

def save_todo(todo):
    new_todo = Todo(todo=todo)
    db.session.add(new_todo)
    db.session.commit()

if __name__ == "__main__":
    db.create_all()   

    port = 7070

    try:
        port = sys.argv[1:][0]
    except:
        pass
    
    host = "0.0.0.0" 
    print("In-memory backend at port", port) 
    from waitress import serve  
    serve(app, host=host, port=port)
    