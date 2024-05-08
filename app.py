from flask import Flask

app = Flask ('Olá ')

@app.route('/')
def ola():
    return "ola mundo, me chamo kennedy da paixao sales"