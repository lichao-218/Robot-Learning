# -*- coding: utf-8 -*-

def P(pose,sleep):
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
    time.sleep(5)
    
#moves robot to pose2    
    pose2 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose2)
    x = str(float(x) - 0.013)
    z = str(float(z) - 0.060)
    p = pose2.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose2 = ' '.join(p)
    s.send (bytes(pose2, 'utf8') + (bytes('\n', 'utf8')))
    #s.send (bytes('movel(p[-0.09292-0.013, 0.658, 0.79831-0.06, 3.9322, 1.6518, 1.6554], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(2.5)


#moves robot to pose3    
    pose3 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose3)
    y = str(float(y) - 0.038)
    z = str(float(z) - 0.030)
    p = pose3.split(' ')
    p[1] = y + ','
    p[2] = z + ','
    pose3 = ' '.join(p)
    s.send (bytes(pose3, 'utf8') + (bytes('\n', 'utf8')))
    #s.send (bytes('movel(p[-0.09292, 0.62, 0.79831-0.03, 3.9322, 1.6518, 1.6554], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)
    
#moves robot to pose4 
    pose4 = pose1
    s.send (bytes(pose4, 'utf8') + (bytes('\n', 'utf8')))
    #s.send (bytes('movel(p[-0.09292-0.013, 0.658, 0.79831, 3.9322, 1.6518, 1.6554], a=0.5, v=0.5)', 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(1.5)

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
    time.sleep(5)
    
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


