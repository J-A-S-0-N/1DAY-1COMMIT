import novation_launchpad as launchpad
import random
from time import sleep
import keyboard
lp1 = 4
lp2 = 5

lp = launchpad.LaunchpadPro()
if lp.Open( 0, "Pro" ):
	print( " - Launchpad Pro: OK" )
else:
	print( " - Launchpad Pro: ERROR" )

a1 = random.randint(1,7)
b1 = random.randint(1,7)
lp1ab = True

a2 = random.randint(1,7)
b2 = random.randint(1,7)
lp2ab = True

a3 = random.randint(1,7)
b3 = random.randint(1,7)
lp3ab = True

a4 = random.randint(1,7)
b4 = random.randint(1,7)
lp4ab = True

a5 = random.randint(1,7)
b5 = random.randint(1,7)
lp5ab = True

a6 = random.randint(1,7)
b6 = random.randint(1,7)
lp6ab = True

move = False

def led():
	lp.LedCtrlXYByRGB( a1, b1, [63, 0, 0])   
	lp.LedCtrlXYByRGB( a2, b2, [63, 0, 0])   
	lp.LedCtrlXYByRGB( a3, b3, [63, 0, 0])  
	lp.LedCtrlXYByRGB( a4, b4, [63, 0, 0])  
	lp.LedCtrlXYByRGB( a5, b5, [63, 0, 0])  
	lp.LedCtrlXYByRGB( a6, b6, [63, 0, 0])


def check():
	if lp1 == a1 and lp2 == a1:
		lp1ab = False
	elif lp1 == a2 and lp2 == b2:
		lp2ab = False
	elif lp1 == a3 and lp2 == b3:
		lp3ab = False
	elif lp1 == a4 and lp2 == b4:
		lp3ab = False
	elif lp1 == a5 and lp2 == b5:
		lp4ab = False
	elif lp1 == a6 and lp2 == b6:
		lp6ab = False
def check_del():
	if lp1ab == False:
		lp.LedCtrlXYByRGB( a1, b1, [63, 0, 0])   
		lp.LedCtrlXYByRGB( a2, b2, [63, 0, 0])   
		lp.LedCtrlXYByRGB( a3, b3, [63, 0, 0])  
		lp.LedCtrlXYByRGB( a4, b4, [63, 0, 0])  
		lp.LedCtrlXYByRGB( a5, b5, [63, 0, 0])  
		lp.LedCtrlXYByRGB( a6, b6, [63, 0, 0])


def main():
	while True:
		lp.ButtonFlush()
		lp.LedAllOn(3)
		led()
		check()
		lp.LedCtrlXYByRGB( lp1, lp2, [0, 63, 0])

		lp2 += 1

		sleep(0.5)
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
