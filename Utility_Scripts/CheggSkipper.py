from pynput import keyboard
import pyautogui as p
def skipButton():
	p.click(803,533)#i dont have subject knowledge 
	p.click(498,1043)#Skip directly
	p.click(1447,848)#submit

def answerButton():
	p.click(336,1043)#answer to solve the question
def exitButton():
	p.click(597,1035)#Exit from the question
def on_press(key):
	try:
		k=key.char
	except:
		k=key.name
	if k=="1":
		skip()#when user press 1 then directly skipped 
	if k=="2":
		answer()#when user press 2 then directly go to answer page
	if k=="3":
		exit()#when it is 3 then directly exit from the question
l=keyboard.Listener(on_press=on_press)
l.start()
l.join()