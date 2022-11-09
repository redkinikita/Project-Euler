l=[]
for i in range(100,1000):
	for j in range(i,1000):
		k=i*j
		k=str(k)
		if k[:]==k[::-1]:
			l.append(int(k))
print(max(l))
			