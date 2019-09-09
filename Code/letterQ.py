# -*- coding: utf-8 -*-

def Q(pose,sleep):
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

##move robot to writing start position
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose)
    s.send (bytes(pose, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(5)

#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew = posea + posemid
    posenew = list(posenew)
    posenew[4] = 'c'
    posenew = ''.join(posenew)
    
#move robot to posenew
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew)
    x = str(float(x) - 0.024)
    z = str(float(z) - 0.03)
    x1 = str(float(x1) + 0.00)
    z1 = str(float(z1) - 0.06)
    p = posenew.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew = ' '.join(p)
    s.send (bytes(posenew, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3.5)

#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew1 = posea + posemid
    posenew1 = list(posenew1)
    posenew1[4] = 'c'
    posenew1 = ''.join(posenew1)
    
#move robot to posenew1
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew1)
    x = str(float(x) + 0.024)
    z = str(float(z) - 0.03)
    x1 = str(float(x1) + 0.00)
    z1 = str(float(z1) + 0.00)
    p = posenew1.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew1 = ' '.join(p)
    s.send (bytes(posenew1, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3.5)
    
#moves robot to pose1   
    pose1 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1)
    y = str(float(y) - 0.034)
    z = str(float(z) - 0.030)
    p = pose1.split(' ')
    p[1] = y + ','
    p[2] = z + ','
    pose1 = ' '.join(p)
    s.send (bytes(pose1, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2)

#moves robot to pose2   
    pose2 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose2)
    x = str(float(x) + 0.004)
    z = str(float(z) - 0.040)
    p = pose2.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose2 = ' '.join(p)
    s.send (bytes(pose2, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2)

#moves robot to pose3
    pose3 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose3)
    x = str(float(x) + 0.025)
    z = str(float(z) - 0.060)
    p = pose3.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose3 = ' '.join(p)
    s.send (bytes(pose3, 'utf8') + (bytes('\n', 'utf8')))
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
