l=list()
for i in range(10,21):
	l.append(i)


i=2520
j=1
while j!=10:
	if i%l[j]==0:
		j+=1
	else:
		j=1
		i+=2520
print(i)
