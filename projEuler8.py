import time
t=time.time()
i=p=k=0
s=1
f=open('num.txt')
line=f.readline()
p=len(line)
while i<(p-13):
	for j in range(i,i+13):
		s*=int(line[j])
	if s>k:
		k=s
	i+=1
	s=1
print(k)
f.close()
print('----%s seconds----'%(time.time()-t))
