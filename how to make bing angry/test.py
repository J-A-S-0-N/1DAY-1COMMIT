import keyboard
import pyautogui

def exit():
	if keyboard.is_pressed("q"):
		quit()

def main():
	while True:
		exit()

if __name__ == "__main__":
	main() 