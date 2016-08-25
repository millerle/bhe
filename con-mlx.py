import sys
import telnetlib
#import ipaddr

from st2actions.runners.pythonrunner import Action 


class ConMlx(Action):


	def run(self,host,username,password,enable,tn):

		host = raw_input("Please enter IP: ")
		username = raw_input("Please enter Username: ")
		password = raw_input("Please enter Password: ")
		enable = raw_input("Please enter the enable password: ")
		tn = telnetlib.Telnet(host, 23, 5)
		tn.expect([">"])
		tn.write("enable\r\n")

		if      tn.expect(["#"]):
			returnvalue = 1
			returnstring = "Script exited normally"
			tn.write("exit\r\n")
		else:
			returnvalue = 0 
			returnstring = "Superuser password wrong"

		return (returnvalue, returnstring)
	
