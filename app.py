from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

    return 'Hello Dosto, This is Purvesh Shapariya, welcome to DevOps Zero To Hero (Junoon  Batch 9)'
    return 'Hello Dosto, welcome to DevOps Zero To Hero (Junoon  Batch 9)\nI’m Purvesh, an aspiring DevOps Engineer focused on optimizing workflows and delivering scalable solutions. Passionate about continuous improvement in IT.'

@app.route('/health')
def health():
    return 'Server is up and running'
