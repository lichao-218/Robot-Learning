# -*- coding: utf-8 -*-

def Three(pose,sleep):
#establish connection between robot and computer
    from Connection import HOST, PORT, socket, time, re
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

#move robot to posestart
    posestart = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posestart)
    y = str(float(y) - 0.100)
    p = posestart.split(' ')
    p[1] = y + ','
    posestart = ' '.join(p)
    s.send (bytes(posestart, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(sleep)

#moves robot to pose1   
    pose1 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1)
    x = str(float(x) - 0.013)
    z = str(float(z))
    p = pose1.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose1 = ' '.join(p)
    s.send (bytes(pose1, 'utf8') + (bytes('\n', 'utf8')))
    #s.send (bytes('movel(p[-0.0929-0.013, 0.658, 0.79831, 3.9322, 1.6518, 1.6554], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)

#moves robot to pose5    
    pose5 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose5)
    x = str(float(x) + 0.010)
    p = pose5.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose5 = ' '.join(p)
    s.send (bytes(pose5, 'utf8') + (bytes('\n', 'utf8')))
    #s.send (bytes('movel(p[-0.09292-0.003, 0.658, 0.79831, 3.9322, 1.6518, 1.6554], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1)

#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew = posea + posemid
    posenew = list(posenew)
    posenew[4] = 'c'
    posenew = ''.join(posenew)

#move robot to posenew
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew)
    x = str(float(x) + 0.022)
    z = str(float(z) - 0.014)
    x1 = str(float(x1) + 0.010)
    z1 = str(float(z1) - 0.028)
    p = posenew.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew = ' '.join(p)
    s.send (bytes(posenew, 'utf8') + (bytes('\n', 'utf8')))
    #s.send (bytes('movec(p[-0.09292+0.011, 0.658, 0.79831-0.015, 3.9322, 1.6518, 1.6554], p[-0.09292-0.003, 0.658, 0.79831-0.027, 3.9322, 1.6518, 1.6554], a=0.25, v=0.15)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(4)
    
#moves robot to pose6   
    pose6 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose6)
    x = str(float(x) - 0.013)
    z = str(float(z) - 0.028)
    p = pose6.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose6 = ' '.join(p)
    s.send (bytes(pose6, 'utf8') + (bytes('\n', 'utf8')))
    #s.send (bytes('movel(p[-0.09292-0.013, 0.658, 0.79831-0.03, 3.9322, 1.6518, 1.6554], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)

#moves robot to pose7   
    pose7 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose7)
    x = str(float(x) + 0.010)
    z = str(float(z) - 0.028)
    p = pose7.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose7 = ' '.join(p)
    s.send (bytes(pose7, 'utf8') + (bytes('\n', 'utf8')))  
    #s.send (bytes('movel(p[-0.09292-0.003, 0.658, 0.79831-0.03, 3.9322, 1.6518, 1.6554], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)

#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew1 = posea + posemid
    posenew1 = list(posenew1)
    posenew1[4] = 'c'
    posenew1 = ''.join(posenew1)  
#move robot to posenew1
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew1)
    x = str(float(x) + 0.022)
    z = str(float(z) - 0.045)
    x1 = str(float(x1) + 0.010)
    z1 = str(float(z1) - 0.060)
    p = posenew1.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew1 = ' '.join(p)
    s.send (bytes(posenew1, 'utf8') + (bytes('\n', 'utf8')))    
    #s.send (bytes('movec(p[-0.09292+0.012, 0.658, 0.79831-0.045, 3.9322, 1.6518, 1.6554], p[-0.09292-0.001, 0.658, 0.79831-0.06, 3.9322, 1.6518, 1.6554], a=0.25, v=0.15)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(4)
    
#moves robot to pose8   
    pose8 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose8)
    x = str(float(x) - 0.013)
    z = str(float(z) - 0.06)
    p = pose8.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose8 = ' '.join(p)
    s.send (bytes(pose8, 'utf8') + (bytes('\n', 'utf8')))     
    #s.send (bytes('movel(p[-0.09292-0.013, 0.658, 0.79831-0.06, 3.9322, 1.6518, 1.6554], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2)

#return to poseend
    poseend = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", poseend)
    x = str(float(x) + 0.034)
    y = str(float(y) - 0.100)
    p = poseend.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[1] = y + ','
    poseend = ' '.join(p)
    s.send (bytes(poseend, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)

#halt
    s.send(bytes("halt",'utf8') + bytes("\n", 'utf8'))  


