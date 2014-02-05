from flask import Flask, render_template, request, redirect, url_for, abort, session
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/on')
def turnon():
  os.system("sudo python /home/pi/buditap/buditap.py start")
  return "on"

@app.route('/off')
def turnoff():
  os.system("sudo python /home/pi/buditap/buditap.py stop")
  # kill readtilt.py
  return "off"

if __name__ == "__main__":
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0', port=80, debug=True)
