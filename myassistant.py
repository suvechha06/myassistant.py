import pyttsx3
import os

pyttsx3.speak("WELCOME TO MY SYSTEM.")

while True:
	print()
	print("Hey! What can I do for you?")
	print("Chat with me about your requirements : " , end=' ')
	p=input()
	p.lower()
	
	
	if (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("chrome" in p) or ("browser" in p) or ("google" in p)):
		os.system("chrome") 
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("chrome" in p) or ("browser" in p) or ("gmail" in p)):
		os.system("chrome gmail.com")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("chrome" in p) or ("browser" in p) or ("yahoo" in p)):
		os.system("chrome yahoo.com")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("chrome" in p) or ("browser" in p) or ("amazon" in p) or ("shopping" in p) or ("website" in p)):
		os.system("chrome amazon.com")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("chrome" in p) or ("browser" in p) or ("flipkart" in p) or ("shopping" in p) or ("website" in p)):
		os.system("chrome flipkart.com")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("chrome" in p) or ("browser" in p) or ("facebook" in p)):
		os.system("chrome facebook.com")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("chrome" in p) or ("browser" in p) or ("youtube" in p)):
		os.system("chrome youtube.com")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("notepad" in p) or ("text" in p) or ("editor" in p)):
		os.system("notepad")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("media" in p) or ("player" in p) or ("windows" in p)):
		os.system("wmplayer")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("visual" in p) or ("studio" in p) or ("code" in p) or ("ide" in p)):
		os.system("code")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("anaconda" in p) or ("python" in p) or ("jupyter" in p) or ("notebook" in p)):
		os.system("anaconda-navigator-script")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and ("vlc" in p) and (("media" in p) or ("player" in p)):
		os.system('vlc')
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("firefox" in p) or ("browser" in p)):
		os.system("firefox")
	elif (("run" in p) or ("open" in p) or ("execute" in p) or ("play in p") or ("help" in p) or ("opening" in p) or ("executing" in p) or ("running" in p)) and (("sql" in p) or ("mysql" in p) or ("workbench" in p)):
		os.system("MySQLWorkbench.exe")
	elif (("don't" in p) or ("not" in p)) and (("chrome" in p) or ("gmail" in p) or ("google" in p) or ("browser" in p) or ("yahoo" in p) or ("flipkart" in p) or ("amazon" in p) or ("shopping" in p) or ("website" in p) or ("facebook" in p) or ("youtube" in p) or ("notepad" in p) or ("text" in p) or ("editor" in p) or ("media" in p) or ("player" in p) or ("windows" in p) or ("visual" in p) or ("studio" in p) or ("code" in p) or ("ide" in p) or ("anaconda" in p) or ("python" in p) or ("vlc" in p) or ("firefox" in p) or ("sql" in p) or ("workbench" in p) or ("mysql" in p) or ("shell" in p)):
		print("ok! any other requirement?") 	
	elif ("exit" in p) or ("quit" in p) or ("stop" in p) or ("go" in p) or ("back" in p) or ("thankyou" in p):
		break
	else:
		print(" sorry requirement cannot be processed ") 
	