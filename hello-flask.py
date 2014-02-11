from flask import Flask, render_template, request, redirect, url_for, abort, session
import os
app = Flask(__name__)

@app.route('/')
def home():
    if os.path.isfile("/var/run/buditap.pid"):
      isOn = "on"
    else:
      isOn = "off"
    return render_template('index.html', isRunning=isOn)

@app.route('/on')
def turnon():
  os.system("sudo python /home/pi/buditap/buditap.py start")
  return "buditap is currently on"

@app.route('/off')
def turnoff():
  os.system("sudo python /home/pi/buditap/buditap.py stop")
  return "buditap is currently off"

@app.route('/theme/<theme_name>')
def themepicker(theme_name):
  # do change theme somehow.  Make it happen Andrew!
  return theme_name

@app.route('/volume/<int:level>')
def volumen(level):
  os.system("vol %d" % level)
  return 'volume set to %d' % level

if __name__ == "__main__":
    app.debug = True
    app.run()
    #app.run(host='0.0.0.0', port=80, debug=True)
