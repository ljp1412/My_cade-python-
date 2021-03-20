# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
import time

def legendre(n,m,x):
    s=np.zeros((n+1,m+1))
    for k in range(0,m+1):
        if k==0:
            s[0,k]=1
            s[1,k]=x
            for j in range(1,n):
                s[j+1,k]=((2*j+1)*x*s[j,k]-j*s[j-1,k])/(j+1)
        else:
            s[0,k]=0
            if k==1:
                s[1,k]=1
            else:
                s[1,k]=0
            for j in range(1,n):
                s[j+1,k]=(2*j+1)*s[j,k-1]+s[j-1,k]
    return s[n,m]

n=20
m=8

x=np.arange(-1,1.01,0.01)
y=[]

for j in range(0,201):
    y.append(legendre(n,m,x[j]))
    
pl.plot(x,y)

    

