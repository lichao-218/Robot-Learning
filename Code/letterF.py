# -*- coding: utf-8 -*-

def F(pose,sleep):
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
    time.sleep(4)

#moves robot to pose1    
    pose1 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1)
    z = str(float(z) - 0.060)
    p = pose1.split(' ')
    p[2] = z + ','
    pose1 = ' '.join(p)
    s.send (bytes(pose1, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2.5)

#moves robot to pose2   
    pose2 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose2)
    y = str(float(y) - 0.038)
    z = str(float(z) - 0.030)
    p = pose2.split(' ')
    p[1] = y + ','
    p[2] = z + ','
    pose2 = ' '.join(p)
    s.send (bytes(pose2, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)
    
#moves robot to pose3
    pose3 = pose
    s.send (bytes(pose3, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)

#moves robot to pose4    
    pose4 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose4)
    x = str(float(x) + 0.035)
    p = pose4.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose4 = ' '.join(p)
    s.send (bytes(pose4, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2.5)
 
#moves robot to pose5  
    pose5 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose5)
    x = str(float(x) + 0.017)
    y = str(float(y) - 0.038)
    z = str(float(z) - 0.015)
    p = pose5.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[1] = y + ','
    p[2] = z + ','
    pose5 = ' '.join(p)
    s.send (bytes(pose5, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)
    
#moves robot to pose6   
    pose6 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose6)
    z = str(float(z) - 0.030)
    p = pose6.split(' ')
    p[2] = z + ','
    pose6 = ' '.join(p)
    s.send (bytes(pose6, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)
    
#moves robot to pose7
    pose7 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose7)
    x = str(float(x) + 0.030)
    z = str(float(z) - 0.030)
    p = pose7.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose7 = ' '.join(p)
    s.send (bytes(pose7, 'utf8') + (bytes('\n', 'utf8')))
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
    time.sleep(2.5)

#halt
    s.send(bytes("halt",'utf8') + bytes("\n", 'utf8'))  