def fibo(p,fsum,f1,f2):
	x=4*(10**6)
	while (f1+f2)<x:
		fsum=f1+f2
		if fsum%2==0:
		 p+=fsum
		print(fsum)
		f1=f2
		f2=fsum 
	print(p)
fibo(0,0,1,1)
