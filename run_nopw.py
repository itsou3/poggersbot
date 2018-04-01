#Python 2.7 Twitch/IRC Chat Bot
#This bot can read chat and print it to the console, send messages

import random
import sys
import socket
import time
import threading

#Parameters should all be in lowercase
HOST ="irc.twitch.tv"
PORT = 6667
PASS = "oauth:" #include account/channel
NICK = ""
CHANNEL = ""

random_messages = ["Hello",
"Welcome",
"Not a bot :)"]

class IRC:
	irc = socket.socket()

	def __init__(self):
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self, HOST, PORT, PASS, NICK, CHANNEL):
		#IRC protocol for connecting to chat
		print "Attempting to connect to: #" + CHANNEL
		self.irc.connect((HOST, PORT)) 
		self.irc.send("PASS " + PASS + "\r\n") 
		self.irc.send("NICK " + NICK + "\r\n")
		self.irc.send("JOIN #" + CHANNEL + "\r\n")

	def get_text(self):
		# Gets chat and whatever IRC messages available
		text=self.irc.recv(2040)
		if text.find("PING") != -1:
			self.irc.send("PONG " + text.split()[1] + "rn")
		return text

	def get_chat(self):
		# prints chat to console in a clean format
		while True:
			try:
				t = self.get_text().split()
				if "PRIVMSG" in t:	
					cleantext = " ".join(t[t.index("PRIVMSG"):])
					print cleantext
			except Exception:
				sys.exit(1)

	def send(self, CHANNEL, msg):
		tempmsg = "PRIVMSG #" + CHANNEL  + " :" + msg
		self.irc.send(tempmsg + "\r\n")
		print "Sent: " + msg

	def reply(self, CHANNEL, query, reply):
		pass

	def timemessage(self):
		while True:
			rtime = random.randint(30, 90)
			rmsg = random.choice(random_messages) 
			time.sleep(rtime)
			self.send(CHANNEL, rmsg)
			

#Start the bot
wb = IRC()
wb.connect(HOST, PORT, PASS, NICK, CHANNEL)
wb.send(CHANNEL, "MrDestructoid /")

#Infinite loops are ran simultaneously 
thread1 = threading.Thread(target=wb.get_chat)
thread1.start()
thread2 = threading.Thread(target=wb.timemessage)
thread2.start()
