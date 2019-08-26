# -*- coding: utf-8 -*-

def J(pose,sleep):
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

#alter writing start position
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose)
    x = str(float(x) - 0.017)
    p = pose.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose = ' '.join(p)

#moves robot to posep  
    posep = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posep)
    x = str(float(x) - 0.003)
    p = posep.split(' ')
    p[0] = 'movel(p[' + x + ','
    posep = ' '.join(p)
    s.send (bytes(posep, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(4)
    
#moves robot to pose1  
    pose1 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1)
    x = str(float(x) + 0.037)
    p = pose1.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose1 = ' '.join(p)
    s.send (bytes(pose1, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2.5)
    
#moves robot to pose2
    pose2 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose2)
    x = str(float(x) + 0.025)
    y = str(float(y) - 0.038)
    p = pose2.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[1] = y + ','
    pose2 = ' '.join(p)
    s.send (bytes(pose2, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2.5)

#moves robot to pose3
    pose3 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose3)
    x = str(float(x) + 0.017)
    p = pose3.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose3 = ' '.join(p)
    s.send (bytes(pose3, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2.5)
    
#moves robot to pose4  
    pose4 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose4)
    x = str(float(x) + 0.017)
    z = str(float(z) - 0.048)
    p = pose4.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose4 = ' '.join(p)
    s.send (bytes(pose4, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2.5)
    
#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew = posea + posemid
    posenew = list(posenew)
    posenew[4] = 'c'
    posenew = ''.join(posenew)
    
#moves robot to newpose
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew)
    x = str(float(x) + 0.009)
    z = str(float(z) - 0.058)
    x1 = str(float(x1) - 0.012)
    z1 = str(float(z1) - 0.040)
    p = posenew.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew = ' '.join(p)
    s.send (bytes(posenew, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)

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
