from flask import Flask
from flask import render_template, url_for, redirect
from flask.ext.foundation import Foundation
from dockerGateway.manager import DockerManager
from docker import Client

app = Flask(__name__)
Foundation(app)
app.config.from_pyfile('dockerwebuicfg.py', silent=True)
c = DockerManager(Client(app.config['DOCKER_URI']))

@app.route('/')
def home():
    msg = c.containers(all=True)
    return render_template('home.html', msg = msg)

@app.route('/start/<containerId>')
def start(containerId):
    c.start(containerId)
    return redirect(url_for('home'))

@app.route('/stop/<containerId>')
def stop(containerId):
    c.stop(containerId)
    return redirect(url_for('home'))

@app.route('/info/<containerId>')
def info(containerId):
    info = c.inspect_container(containerId)
    return render_template('info.html', info = info)

@app.route('/config/<containerId>')
def config(containerId):
    return "Not Implemented"

if __name__ == '__main__':
    app.debug = True
    app.run()
