# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:04:46 2015

@author: arjunr
"""


import numpy as np
import matplotlib.pyplot as plt

file_loc='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/profile100.data'
f = open(file_loc,"r+")
lines=f.readlines()
open('profile100newfull.dat', 'w').writelines(lines[6:])
file_loc_new='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/profile100newfull.dat'
d=np.loadtxt(file_loc_new)
x=open('profile100finalfull.dat','w')
file_loc_final='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/profile100finalfull.dat'
nrows=(np.int(d.shape[0]))
nisotopes=19
x.write('%d' %nrows)
x.write('\s')
x.write('%d' %nisotopes)
x.write('\n')
x.write('%f' %1.0)
x.write('\s')
x.write('%f' %3.0)
x.write('\s')
x.write('%f' %4.0)
x.write('\s')
x.write('%f' %12.0)
x.write('\s')
x.write('%f' %14.0)
x.write('\s')
x.write('%f' %16.0)
x.write('\s')
x.write('%f' %20.0)
x.write('\s')
x.write('%f' %24.0)
x.write('\s')
x.write('%f' %28.0)
x.write('\s')
x.write('%f' %32.0)
x.write('\s')
x.write('%f' %36.0)
x.write('\s')
x.write('%f' %40.0)
x.write('\s')
x.write('%f' %44.0)
x.write('\s')
x.write('%f' %48.0)
x.write('\s')
x.write('%f' %56.0)
x.write('\s')
x.write('%f' %52.0)
x.write('\s')
x.write('%f' %54.0)
x.write('\s')
x.write('%f' %56.0)
x.write('\s')
x.write('%f' %56.0)
x.write('\s')

x.write('\n')

x.write('%f' %1.0)
x.write('\s')
x.write('%f' %2.0)
x.write('\s')
x.write('%f' %2.0)
x.write('\s')
x.write('%f' %6.0)
x.write('\s')
x.write('%f' %7.0)
x.write('\s')
x.write('%f' %8.0)
x.write('\s')
x.write('%f' %10.0)
x.write('\s')
x.write('%f' %12.0)
x.write('\s')
x.write('%f' %14.0)
x.write('\s')
x.write('%f' %16.0)
x.write('\s')
x.write('%f' %18.0)
x.write('\s')
x.write('%f' %20.0)
x.write('\s')
x.write('%f' %22.0)
x.write('\s')
x.write('%f' %24.0)
x.write('\s')
x.write('%f' %24.0)
x.write('\s')
x.write('%f' %26.0)
x.write('\s')
x.write('%f' %26.0)
x.write('\s')
x.write('%f' %26.0)
x.write('\s')
x.write('%f' %28.0)
x.write('\s')

x.write('\n')

for i in range (0, nrows):
    mass=(d[i,54])*(1.98855*10**33)
    x.write('%f' %mass)
    x.write('\t')
    radius=(d[i,22])*(6.955*10**10)
    x.write('%f' %radius)
    x.write('\t')
    protf=(d[i,62])
    x.write('%f' %protf)
    x.write('\t')
    he3f=(d[i,63])
    x.write('%f' %he3f)
    x.write('\t')
    he4f=(d[i,64])
    x.write('%f' %he4f)
    x.write('\t')
    c12f=(d[i,65])
    x.write('%f' %c12f)
    x.write('\t')
    n14f=(d[i,66])
    x.write('%f' %n14f)
    x.write('\t')
    o16f=(d[i,67])
    x.write('%f' %o16f)
    x.write('\t')
    ne20f=(d[i,68])
    x.write('%f' %ne20f)
    x.write('\t')
    mg24f=(d[i,69])
    x.write('%f' %mg24f)
    x.write('\t')
    si28f=(d[i,70])
    x.write('%f' %si28f)
    x.write('\t')
    s32f=(d[i,71])
    x.write('%f' %s32f)
    x.write('\t')
    ar36f=(d[i,72])
    x.write('%f' %ar36f)
    x.write('\t')
    ca40f=(d[i,73])
    x.write('%f' %ca40f)
    x.write('\t')
    ti44f=(d[i,74])
    x.write('%f' %ti44f)
    x.write('\t')
    cr48f=(d[i,75])
    x.write('%f' %cr48f)
    x.write('\t')
    cr56f=(d[i,76])
    x.write('%f' %cr56f)
    x.write('\t')
    fe52f=(d[i,77])
    x.write('%f' %fe52f)
    x.write('\t')
    fe54f=(d[i,78])
    x.write('%f' %fe54f)
    x.write('\t')
    fe56f=(d[i,79])
    x.write('%f' %fe56f)
    x.write('\t')
    ni56f=(d[i,80])
    x.write('%f' %ni56f)
    x.write('\n')
    
x.close() 
    
    
    
