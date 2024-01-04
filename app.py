from flask import request, Flask
import json
import socket

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
    container_id = socket.gethostname()
    return f'Salam alikom, this is container {container_id} :) '

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0', port=5000)