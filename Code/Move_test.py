# -*- coding: utf-8 -*-

import socket
import time
HOST = "..."
PORT = ...
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))


s.send (bytes('movel(p[-0.40, 0.205, 0.798, 3.9322, 1.6518, 1.6554], a=0.75, v=0.75)', 'utf8') + (bytes('\n', 'utf8')))
time.sleep(8)
s.send (bytes('movel(p[-0.09292, 0.29784, 0.79831, 3.9322, 1.6518, 1.6554], a=0.75, v=0.75)', 'utf8') + (bytes('\n', 'utf8')))
time.sleep(6)
s.send (bytes('movel(p[0.0, 0.3, 0.5, 0.0, 3.14, 0.0], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
time.sleep(7)

f = open ("open.script", "rb")       
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
time.sleep(5)

s.close()

x = '-0.143'
y = '0.652'
z = '0.698'