import novation_launchpad as launchpad
import random
from time import sleep
import keyboard

lp = launchpad.LaunchpadPro()
if lp.Open( 0, "Pro" ):
	print( " - Launchpad Pro: OK" )
else:
	print( " - Launchpad Pro: ERROR" )

def main():
	while True:
		lp.ButtonFlush()
		lp.LedAllOn(3)
	print("Entering main loop. Press Control-C to exit.")
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		print('')
	finally:
		print("Exit.")
		lp.Reset()
		lp.Close()
if __name__ == '__main__':
	main()
