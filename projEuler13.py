def summa(s):
	f=open('mat.txt','r')
	for line in f:
		s+=line
	return(s)
print(summa(0))