def pancifri(n,su):
	a=[True]*n
	u=0
	e=0
	b=[]
	q=set(str(u))
	for i in range(10,100):
		k=str(i)
		h=set(k)
		c=len(h)
		if c!=2:
			a[i]=False
		for f in range(0,2):
			if int(k[f])==0:
				a[i]=False
	for j in range(100,n):
		m=str(j)
		l=set(m)
		d=len(l)
		if d!=3:
			a[j]=False
		for f in range(0,3):
			if int(m[f])==0:
				a[j]=False
	for i in range(1,100):
		if a[i]:
			for j in range(100,1000):
				if a[j]:
					r=str(i)
					p=str(j)
					x=r+p
					k=len(set(x))
					if k==5:
						o=str(i*j)
						x+=o
						w=set(x)
						if w.isdisjoint(q):
							g=len(set(x))
							if g==9:
								if int(o)<10000:
									b.append(int(o))


	y=[False]+[True]*(10000-1)
	for i in range(1,10):
		if y[i]:
			for j in range(1000,10000):
				m=str(j)
				l=set(m)
				d=len(l)
				if d!=4:
					y[j]=False
				for f in range(0,4):
					if int(m[f])==0:
						y[j]=False
	for i in range(1,10):
		if y[i]:
			for j in range(1000,10000):
				if y[j]:
					r=str(i)
					p=str(j)
					x=r+p
					k=len(set(x))
					if k==5:
						o=str(i*j)
						x+=o
						w=set(x)
						if w.isdisjoint(q):
							g=len(set(x))
							if g==9:
								if int(o)<10000:
									b.append(int(o))
	
	print('Сумма всех пан цифровых =', sum(set(b)))
	print(set(b))
pancifri(1000,0)
