from flask import Flask, jsonify, request, Response, abort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    arg = request.args.get('name')

    if arg is not None:
        return Response("hello " + arg, status=200)
    else:
        return Response("hello anon!", status=200)

if __name__ == "__main__":
    from waitress import serve
    host = "0.0.0.0"
    port = 8080
    print('Server started in port {port}'.format(port=port))
    app.logger.info('Server started at %s:%s', host, port)
    serve(app, host=host, port=port)
    