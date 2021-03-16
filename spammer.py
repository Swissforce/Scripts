import pyautogui, time, sys, os.path

def processArguments():
	zeugs = ""
	iterationen = 1
	wartenAnfangDauer = 0
	# wartenLoopDauer = 2 geht nicht weil time.sleep() alles auf einmal schläft und dann alles gleichzeitig ausprinted
	boolEnter = True

	


	#Falls nicht jeder Parameter gefüllt ist	
	try:
		if sys.argv[1]:
			zeugs = sys.argv[1]
			
			if sys.argv[2]:
				iterationen = int(sys.argv[2])

				if sys.argv[3]:
					wartenAnfangDauer = int(sys.argv[3])

					if sys.argv[4] == "False" or sys.argv[4] == 0:
						boolEnter = False

	except:
		pass

	finally:
		return [zeugs,iterationen,wartenAnfangDauer,boolEnter]


def spammer(args):
	zeugs = args[0]
	iterationen = args[1]
	wartenAnfangDauer = args[2]
	boolEnter = args[3]

	if zeugs:
		if os.path.isfile(zeugs):
			time.sleep(wartenAnfangDauer)

			f = open(zeugs,"rt")

			for iters in range(iterationen):
				f.seek(0)
				for x in f:
					pyautogui.typewrite(x)

					if boolEnter:
						pyautogui.press("enter")

					#time.sleep(wartenLoopDauer)

		else:
			time.sleep(wartenAnfangDauer)

			for x in range(iterationen):
				pyautogui.typewrite(zeugs)
				
				if boolEnter:
					pyautogui.press("enter")

				#time.sleep(wartenLoopDauer)

spammer(processArguments())