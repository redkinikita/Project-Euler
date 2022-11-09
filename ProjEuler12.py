def treug(n):
	summa=0
	deliteli=0
	a=[]
	for i in range(1,n):
		summa+=i
		a.append(summa)
	s=len(a)//2

	for i in range(1,n-1):
		for j in range(1,n-1):
				if a[j]>j:

				else:
					if a[j]%j==0:
						deliteli+=1
					print(deliteli) 

		if deliteli>=500:
			print (a[i])
		else:
			deliteli=0

treug(100000)
			
