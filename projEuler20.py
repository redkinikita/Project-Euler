import math

n=math.factorial(100)
n=str(n)
p=len(n)
i=0
s=0
while i<p:
	s+=(int(n[i]))
	i+=1
print(s)