# -*- coding: utf-8 -*-

def V(pose,sleep):
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
    x = str(float(x) - 0.017)
    p = pose.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose = ' '.join(p)
    s.send (bytes(pose, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3.5)

#moves robot to pose1    
    pose1 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1)
    x = str(float(x) + 0.017)
    z = str(float(z) - 0.060)
    p = pose1.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose1 = ' '.join(p)
    s.send (bytes(pose1, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2.5)

#moves robot to pose2   
    pose2 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose2)
    x = str(float(x) + 0.034)
    p = pose2.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose2 = ' '.join(p)
    s.send (bytes(pose2, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)
 
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

