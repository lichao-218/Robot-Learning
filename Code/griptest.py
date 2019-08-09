# -*- coding: utf-8 -*-

import os
os.chdir("your directory")
# Echo client program
import socket
import time

HOST = " The UR IP address "
PORT = " UR secondary client "
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

f = open ("activate.script", "rb")   #Robotiq Gripper
#f = open ("setzero.script", "rb")  #Robotiq FT sensor

l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)

s.send (bytes('halt','utf8') + bytes('\n', 'utf8'))
s.close()