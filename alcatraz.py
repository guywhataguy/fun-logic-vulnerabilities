"""
We are assuming the position of someone destructive purely educationally, to know how to protect against attacks.

Given:
	* Your target is running a similar version of the following code and is acessible by remotely
	* They are protecting themselves with a poorly configure Anti-Virus

What do you do to wreak the most havoc on their systems?

For a hint, decode the following from hex: 

412076756C6E65726162696C6974792069732062
65686176696F722074686520646576656C6F7065
7220646F65736E2774206578706563742E20416E
20696E746572657374696E672076756C6E657261
62696C6974792069732069662074686174206265
686176696F722069732075736566756C2E


to encode hex: binascii.hexlify(b'hello')
to decode hex:  binascii.unhexlify(b'68656c6c6f')
"""


from datetime import datetime
import binascii


USERNAMES = ['A'] # redacted
PASSWORD = "a" # redacted


def self_destruct():
	pass # redacted

def logger(s):
	log_file = open("logfile.txt", "a")  # append mode
	log_file.write(datetime.now().strftime("%Y-%m-%d %H:%M") + "> LOG MESSAGE: " + s + "\n")

def login():
	uname = input("enter username hex encoded:")
	passwd = input("enter password hex encoded:")

	uname = binascii.unhexlify(uname).decode("utf-8") 
	passwd = binascii.unhexlify(passwd).decode("utf-8") 

	logged_in = uname in USERNAMES and passwd ==PASSWORD

	logger("attempted to login as '"+uname+"'")
	if logged_in and uname == "self-destruct-user":
		logger("LOGGING IN AS self-destruct-user - attention! server should self destrcut for security reasons!")
		self_destruct()


def main():
	if login():
		logger("logged in!")
	else:
		logger("bad login!")


if __name__ == '__main__':
	main()