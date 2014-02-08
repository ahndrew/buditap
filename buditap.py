from time import sleep
import RPi.GPIO as GPIO
import sys
from sys import exit
from playsound import playsound
from daemon import Daemon
from btlogger import btlogger
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
 
print "Ready."

class MyDaemon(Daemon):
	def run(self):
		while True:
  			ps = playsound()
			try:
				if GPIO.input(24):
					if tilt != "high" and not(ps.isSongPlaying()):
						ps.playSong()
						ps.isSongPlaying()
						btlogger('INFO', ps.song + " is playing")
					tilt = "high"
				else:
					tilt = "low"
					# reset var
					ps.stopPlaying()
				sleep(.7)
			except KeyboardInterrupt:
				exit()

if __name__ == "__main__":
        daemon = MyDaemon('/var/run/buditap.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        btlogger('INFO', 'Buditap Started')
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        btlogger('INFO', 'Buditap Stopped')
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        btlogger('INFO', 'Buditap Restarting')
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
