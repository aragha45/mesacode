# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:21:24 2015

@author: arjunr
"""

import numpy as np
import matplotlib.pyplot as plt
file_loc='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/DataAnalysis-1/rad_photo.dat'
file_loc_2='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/lum_observed_8.dat'
file_loc_3='C:/Users/arjunr/Documents/Documents/PrincetonUSRP--Summer2015/Project/T_eff_8.dat'
a=np.loadtxt(file_loc)
b=np.loadtxt(file_loc_2)
c=np.loadtxt(file_loc_3)
dims=np.shape(a)
dims=np.array(dims)
time_secs_initial=a[:,0] # sampling times are taken to be the same given that in all parameters files, dtout_scalar = 1.7d3 (1.7*10^3 seconds - 1,700 seconds)
time_secs=time_secs_initial[1:(dims[0]-1)]
time_days=(time_secs)/86400
radii_initial=a[:,1]
radii=radii_initial[1:(dims[0]-1)]
lum_obs_values_initial=b[:,1]
lum_obs_values=lum_obs_values_initial[0:(np.size(time_days))]
T_eff_values=c[:,1]
pi=np.pi
sbconstant=5.670373*(10**-5)
calculated_luminosity_values=[]
for i in range (0,(np.size(T_eff_values)-1)):
    calculated_luminosity_values.append(4*pi*sbconstant*((radii[i])**2)*((T_eff_values[i])**4))

plt.plot(time_days,np.log10(lum_obs_values),'r--',label='actual luminosity values')
plt.plot(time_days,np.log10(calculated_luminosity_values),'b--',label='calculated luminosity values via T_eff and R_photo')
plt.xlim(0,150)
plt.ylim(41.2,42.8)
plt.legend()

plt.show()

lum_obs_values=np.array(np.log10(lum_obs_values))
calculated_luminosity_values=np.array(np.log10(calculated_luminosity_values))
difference_calculations=np.sum(lum_obs_values-calculated_luminosity_values)
print difference_calculations/(np.size(lum_obs_values))