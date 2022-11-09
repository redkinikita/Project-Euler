l=list()
summ=0
sq=0
for i in range(1,101):
	l.append(i)

for i in range(0,100):
	summ+=(l[i]**2)
	sq+=l[i]
res=(sq**2)-summ
print(res)