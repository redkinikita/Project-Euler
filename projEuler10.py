s=0
n=2000000
a=[True]*n
a[0]=a[1]=False
for k in range (2,n):
  if a[k]:
  	s+=k
  	for m in range(2*k,n,k):
  		a[m]=False
print(s)

