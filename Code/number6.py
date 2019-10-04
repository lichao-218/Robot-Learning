# -*- coding: utf-8 -*-

def Six(pose,sleep):
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

#moves robot to pose1   
    pose1 = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1)
    x = str(float(x) - 0.010)
    p = pose1.split(' ')
    p[0] = 'movel(p[' + x + ','
    pose1 = ' '.join(p)
    s.send (bytes(pose1, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)
    
#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew = posea + posemid
    posenew = list(posenew)
    posenew[4] = 'c'
    posenew = ''.join(posenew)
    
#extracted integers from command string
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew)
#changed pose coordinates
    x = str(float(x) - 0.034)
    z = str(float(z) - 0.030)
    x1 = str(float(x1) - 0.010)
    z1 = str(float(z1) - 0.060)
#split up command string to insert changed cooordinates
    p = posenew.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
#put string back together
    posenew = ' '.join(p)
#move robot to second position
    s.send (bytes(posenew, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(5)

#moves robot to pose1b   
    pose1b = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1b)
    x = str(float(x) - 0.009)
    z = str(float(z) - 0.060)
    p = pose1b.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose1b = ' '.join(p)
    s.send (bytes(pose1b, 'utf8') + (bytes('\n', 'utf8')))
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
    x = str(float(x) + 0.003)
    z = str(float(z) - 0.045)
    x1 = str(float(x1) - 0.009)
    z1 = str(float(z1) - 0.030)
    p = posenew1.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew1 = ' '.join(p)
    s.send (bytes(posenew1, 'utf8') + (bytes('\n', 'utf8'))) 
    time.sleep(3)

#moves robot to pose1c   
    pose1c = pose
    x,y,z,rx,ry,rz,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", pose1c)
    x = str(float(x) - 0.012)
    z = str(float(z) - 0.030)
    p = pose1c.split(' ')
    p[0] = 'movel(p[' + x + ','
    p[2] = z + ','
    pose1c = ' '.join(p)
    s.send (bytes(pose1c, 'utf8') + (bytes('\n', 'utf8')))
    time.sleep(3)

#converted movel format to movec
    posea, poseb = pose.split(']')    
    posemid = '], ' + pose[6:]
    posenew2 = posea + posemid
    posenew2 = list(posenew2)
    posenew2[4] = 'c'
    posenew2 = ''.join(posenew2)  
#move robot to posenew2
    x,y,z,rx,ry,rz,x1,y1,z1,rx1,ry1,rz1,a,v = re.findall(r"[-+]?\d*\.\d+|\d+", posenew2)
    x = str(float(x) - 0.024)
    z = str(float(z) - 0.045)
    x1 = str(float(x1) - 0.012)
    z1 = str(float(z1) - 0.060)
    p = posenew2.split(' ')
    p[0] = 'movec(p[' + x + ','
    p[2] = z + ','
    p[6] = ' p[' + x1 + ','
    p[8] = z1 + ','
    posenew2 = ' '.join(p)
    s.send (bytes(posenew2, 'utf8') + (bytes('\n', 'utf8'))) 
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
    




