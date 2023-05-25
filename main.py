from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():

    user_ip = request.remote_addr
    return f'Hello World, tu ip es {user_ip}'