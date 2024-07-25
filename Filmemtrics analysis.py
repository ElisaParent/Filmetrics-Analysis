# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def validate_index(n_expected,n_given):
  if n_given < 1:
    print("If not a metamaterial, is not phyiscally possible.")
    return 1
  elif n_given < (.9*n_expected) or n_given > (1.1*n_expected):
      print("The index of refraction is outside the range of expected values.")
      return 2
  else:
    return 0
n_Si0=1.45
df = pd.read_csv("C:/Users/14086/Downloads/07082024 Oxide Thickness 5 mins 980 C - Sheet1.csv")
print(df.head)

index=list(df.columns)
print(index)
thickness,index_of_refraction,GOF=list(df[index[2]]),list(df[index[3]]),list(df[index[4]])
print(thickness,index_of_refraction,GOF)
neg,outside=0,0
x=0
thick,gof,i=[],[],[]
for n in index_of_refraction:
    validate_index(n_Si0, n)
    if validate_index(n_Si0,n)==1:
        neg=+1
    elif validate_index(n_Si0, n)==2:
        outside+=1 
        thick.append(thickness[x])
        gof.append(GOF[x])
        i.append(n)
    else:
       thick.append(thickness[x])
       gof.append(GOF[x])
       i.append(n)
    x= x +1

print("This is the percentage of samples not physically possible",100*(neg/len(index_of_refraction)),"% and the number of samples with index of refraction off of the assumed index of refraction ",100*(outside/len(index_of_refraction)),"%.")
thick_mean,thick_std=np.mean(thick),np.std(thick)
gof_mean,gof_std=np.mean(gof),np.std(gof)
print("The mean of the thickness is",thick_mean,"and the standard deviation is",thick_std,".")
print("The mean of the goodness of fit is",gof_mean,"and the goodness of fit is",gof_std,".")
x=np.linspace(1,len(gof),len(gof))


fig, axs = plt.subplots(2, 2, layout='constrained')

ax = axs[0][0]
ax.scatter(x,thick)
ax.set_title('Thickness')


ax = axs[0][1]
ax.scatter(x,gof)
ax.set_title('Goodness of Fit')

ax = axs[1][0]
ax.scatter(x,i)
ax.set_title('Index of Refraction')




plt.show()