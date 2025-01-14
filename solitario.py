import numpy as np 



a=[]
a1=1066 #Término inicial
r=(8528/ a1)**(1/3) #Razón constante entre términos
for i in range(10):
    n=i+1
    a.append(round(a1*r**(n-1)))
    print(f'a[{n+1}]={a[i]}') 
