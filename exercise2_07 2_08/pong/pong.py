from flask import Flask, jsonify, request, Response, abort
import time
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from app import app
from app import db
from models import Ping

@app.route('/counter', methods=['GET'])
def get_count():
    counter = read()
    return Response(str(counter), status=200)

@app.route('/', methods=['GET'])
def root():

    counter = read()
    counter = counter + 1
    write()
    response_str = 'I have been ponged {counter} times!'.format(counter=counter)        
    return Response(response_str, status=200)

def write():
    new_timestamp = Ping(timestamp=str(time.time()))
    db.session.add(new_timestamp)
    db.session.commit()
    return
    
def read():
    timestamps = [instance.timestamp for instance in db.session.query(Ping)]
    counter = len(timestamps)    
    return counter

if __name__ == "__main__":

    db.create_all()    

    port = 6060
    host = "0.0.0.0"    
    print('Pong server started in port {port}'.format(port=port))
    from waitress import serve
    serve(app, host=host, port=port)