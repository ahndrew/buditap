from flask import Flask, render_template, request, redirect, url_for, abort, session
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/on')
def turnon():
  return "tap on!"
# load readtilt.py

@app.route('/off')
def turnoff():
  return "tap off!"
# kill readtilt.py

if __name__ == "__main__":
    app.debug = True
    app.run()
    #app.run(host='0.0.0.0', port=, debug=True)