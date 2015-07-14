# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:46:27 2015

@author: arjunr
"""

import numpy as np
import matplotlib.pyplot as plt

file_loc='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/profile100.data'
f = open(file_loc,"r+")
lines=f.readlines()
open('profile100new.dat', 'w').writelines(lines[6:])
file_loc_new='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/profile100new.dat'
d=np.loadtxt(file_loc_new)
x=open('profile100final.dat','w')
file_loc_final='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/profile100final.dat'
nrows=(np.int(d.shape[0]))
x.write('%d' %nrows)
x.write('\n')
for i in range (0, nrows):
    cellind=(d[i,0])
    mass=(d[i,54])*(1.98855*10**33)
    radius=(d[i,22])*(6.955*10**10)
    temperature=(d[i,24])
    density=10**(d[i,2])
    velocity=(d[i,11])
    ye=(d[i,36])
    omega=(d[i,102])
    x.write('%f' %cellind)
    x.write('\t')
    x.write('%f' %mass)
    x.write('\t')
    x.write('%f' %radius)
    x.write('\t')
    x.write('%f' %temperature)
    x.write('\t')
    x.write('%f' %density)
    x.write('\t')
    x.write('%f' %velocity)
    x.write('\t')
    x.write('%f' %ye)
    x.write('\t')
    x.write('%f' %omega)
    x.write('\n')     
    
x.close()

