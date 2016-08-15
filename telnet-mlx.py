#!/usr/bin/python
import sys
import telnetlib

PROMPT = '#'
HOST =  '10.17.138.26'
user = 'lauren'
password = 'brocade'

tn = telnetlib.Telnet(HOST, 23, 5)
tn.write("enable\r\n")
tn.expect(["Password:"])
tn.write("brocade\r\n")
tn.expect(["MLX2#"])
tn.write("skip\r\n")
print tn.expect(["MLX2#"])
print tn.write("show ver\r\n") # Show mac
print tn.expect(["MLX2#"])
tn.write("exit\r\n")
tn.close

