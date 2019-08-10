# -*- coding: utf-8 -*-

import socket
import time

HOST = "UR robot IP"
PORT = port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def Pickup():
    s.send (bytes('movel(p[0.0, 0.3, 0.5, 0.0, 3.14, 0.0], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(4)

    f = open ("act1.script", "rb") 
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    time.sleep(6)

    f = open ("open.script", "rb")       
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    time.sleep(5)
    
    s.send (bytes('movel(p[0.373, 0.225, 0.5, 1.033, -2.579, -2.540], a=0.75, v=0.75)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(5)
    s.send (bytes('movel(p[0.373, 0.305, 0.138, 1.033, -2.579, -2.540], a=0.75, v=0.75)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)
    s.send (bytes('movel(p[0.369, 0.370, 0.138, 1.033, -2.579, -2.540], a=0.75, v=0.75)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2)
    
    g = open ("close.script", "rb") 
    l = g.read(1024)
    while (l):
        s.send(l)
        l = g.read(1024)
    time.sleep(5)
    
    s.send (bytes('movel(p[0.373, 0.305, 0.138, 1.033, -2.579, -2.540], a=0.75, v=0.75)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)
    s.send (bytes('movel(p[0.373, 0.225, 0.5, 1.033, -2.579, -2.540], a=0.75, v=0.75)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)
    s.send (bytes('movel(p[0.0, 0.3, 0.5, 0.0, 3.14, 0.0], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(5)
  
    s.send(bytes("halt",'utf8') + bytes("\n", 'utf8'))  
        
