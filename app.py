from flask import Flask, request
from json import loads

app = Flask(__name__)

@app.route('/')
def route_home():
    return "Hello, world!"

@app.route('/api', methods=['POST'])
def route_api():
    data = {}
    try:
        data = loads(request.data)
    except:
        print("Didn't get a JSON input!")
    return '{"challenge":"35902439"}'

if __name__ == '__main__':
    app.run(port=5000)