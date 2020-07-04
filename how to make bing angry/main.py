import pyautogui


while True:
	for i in range(0,40):
		pyautogui.moveTo(1551,592)
		pyautogui.click()
		pyautogui.write("fu", interval = 0)
		pyautogui.press("enter", interval = 0)
	for  i in range(0,20):
		pyautogui.write("im really sorry", interval = 0 )