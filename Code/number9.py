# -*- coding: utf-8 -*-

def Nine(pose,sleep):
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
    s.send (bytes(pose, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(4)

#moves robot to pose1   
    pose1 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1)
    x = str(float(x) - 0.005)
    p = pose1.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose1 = ' '.join(p)
    s.send (bytes(pose1, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1)

#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew = posea + posemid
    posenew = list(posenew)
    posenew[4] = 'c'
    posenew = ''.join(posenew)

#move robot to posenew1
    posenew1 = posenew
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew1)
    x = str(float(x) - 0.017)
    z = str(float(z) - 0.015)
    x1 = str(float(x1) - 0.005)
    z1 = str(float(z1) - 0.030)
    p = posenew1.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew1 = ' '.join(p)
    s.send (bytes(posenew1, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)

#moves robot to pose2  
    pose2 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose2)
    x = str(float(x) + 0.005)
    z = str(float(z) - 0.030)
    p = pose2.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose2 = ' '.join(p)
    s.send (bytes(pose2, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(4)

#move robot to posenew2
    posenew2 = posenew
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew2)
    x = str(float(x) + 0.017)
    z = str(float(z) - 0.015)
    x1 = str(float(x1) + 0.005)
    z1 = str(float(z1) - 0.000)
    p = posenew2.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew2 = ' '.join(p)
    s.send (bytes(posenew2, 'utf8') + (bytes('\n', 'utf8')))    
    time.sleep(3)

#moves robot to pose3    
    pose3 = pose
    s.send (bytes(pose3, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1)

#moves robot to pose4
    pose4 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose4)
    x = str(float(x) + 0.017)
    y = str(float(y) - 0.038)
    p = pose4.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[1] = y + ','
    pose4 = ' '.join(p)
    s.send (bytes(pose4, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1)

#moves robot to pose5
    pose5 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose5)
    x = str(float(x) + 0.017)
    p = pose5.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose5 = ' '.join(p)
    s.send (bytes(pose5, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1)
    
#moves robot to pose6 
    pose6 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose6)
    x = str(float(x) + 0.017)
    z = str(float(z) - 0.060)
    p = pose6.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose6 = ' '.join(p)
    s.send (bytes(pose6, 'utf8') + (bytes('\n', 'utf8')))
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




