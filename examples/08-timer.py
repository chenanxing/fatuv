from __future__ import print_function
import sys
sys.path.append('.')

import time
import signal
from fatuv import Loop, Timer, Signal

counter = 0

def repeat_callback(handle):
	global counter
	counter += 1	
	if counter < 10:
		print('repeat counter = %d, %s' % (counter, time.strftime('%H:%M:%S')))
	else:
		handle.stop()

def timer_callback(handle):
	global counter
	counter += 1
	if counter < 5:
		print('counter = %d, %s' % (counter, time.strftime('%H:%M:%S')))
	else:
		print('try again()')
		handle.timer_callback = repeat_callback
		handle.repeat   = 3.5 # 3.5s
		handle.again()

def signal_cb(signal_h, signum):
	timer_h.close()
	signal_h.close()

loop = Loop.default_loop()

timer_h = Timer(loop)
timer_h.start(timer_callback, 1.5, 0.5) # timeout = 1.5s, repeat = 0.5s

signal_h = Signal(loop)
signal_h.start(signal_cb, signal.SIGINT)

print('timer start,', time.strftime('%H:%M:%S'))
print('timer repeat =', timer_h.repeat)
loop.run()

