import math

def isint(s):
    return int(s)==float(s) 

for i in range(1,1000):
    for j in range(i,1000):
        p=(i**2)+(j**2)
        s=math.sqrt(p)    
        k=isint(s) 
        if k:
            m=i+j+s
            if m==1000:
                print (i*j*s)
               
