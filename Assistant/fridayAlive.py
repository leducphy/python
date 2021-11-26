#################################################################
#                             _`				                #
#                          _ooOoo_				                #
#                         o8888888o				                #
#                         88" . "88				                #
#                         (| -_- |)				                #
#                         O\  =  /O				                #
#                      ____/`---'\____				            #
#                    .'  \\|     |//  `.			            #
#                   /  \\|||  :  |||//  \			            #
#                  /  _||||| -:- |||||_  \			            #
#                  |   | \\\  -  /'| |   |			            #
#                  | \_|  `\`---'//  |_/ |			            #
#                  \  .-\__ `-. -'__/-.  /			            #
#                ___`. .'  /--.--\  `. .'___			        #
#             ."" '<  `.___\_<|>_/___.' _> \"".			        #
#            | | :  `- \`. ;`. _/; .'/ /  .' ; |		        #
#            \  \ `-.   \_\_`. _.'_/_/  -' _.' /		        #
#=============`-.`___`-.__\ \___  /__.-'_.'_.-'=================#
#                           `=--=-'                          


import speech_recognition
import pyttsx3
from datetime import date, datetime

friday_ear = speech_recognition.Recognizer()
friday_mouth = pyttsx3.init()
friday_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Friday: I'm listening")
		audio = friday_ear.listen(mic)
	print("Friday: ...")

	try:
		user = friday_ear.recognize_google(audio)
	except:
		user = ""

	print("You: " + user)

	if user == "c":
		friday_brain = "i can't hear you, try again"
	elif user == "hello Friday":
		friday_brain = "hello boss"
	elif "today" in user:
		today = date.today()
		friday_brain = today.strftime("%B %d, %Y")
	elif "time" in user:
		now = datetime.now()
		friday_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "bye" or "goodbye" in user:
		friday_brain == "Bye boss"
		friday_mouth.say(friday_brain)
		friday_mouth.runAndWait()
		break
	else:
		friday_brain = "i'm fine thank you and you"
	print("Friday: "+ friday_brain)

	friday_mouth.say(friday_brain)
	friday_mouth.runAndWait()

