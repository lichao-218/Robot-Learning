# -*- coding: utf-8 -*-

def Five(pose,sleep):
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

#move robot to writing start position
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose)
    x = str(float(x) + 0.017)
    p = pose.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose = ' '.join(p)
    s.send (bytes(pose, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(5)
    
#moves robot to pose2    
    pose2 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose2)
    x = str(float(x) - 0.034)
    p = pose2.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose2 = ' '.join(p)
    s.send (bytes(pose2, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)

#moves robot to pose3    
    pose3 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose3)
    x = str(float(x) - 0.034)
    z = str(float(z) - 0.030)
    p = pose3.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose3 = ' '.join(p)
    s.send (bytes(pose3, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2)

#moves robot to pose4    
    pose4 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose4)
    x = str(float(x)- 0.012)
    z = str(float(z) - 0.030)
    p = pose4.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose4 = ' '.join(p)
    s.send (bytes(pose4, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1)

#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew1 = posea + posemid
    posenew1 = list(posenew1)
    posenew1[4] = 'c'
    posenew1 = ''.join(posenew1)  
#move robot to posenew1
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew1)
    x = str(float(x) + 0.000)
    z = str(float(z) - 0.045)
    x1 = str(float(x1) - 0.012)
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
    x = str(float(x) - 0.034)
    z = str(float(z) - 0.060)
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


