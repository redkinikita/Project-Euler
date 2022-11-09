func={}

def Factor(n):
	Ans=[]
	d=2
	while d*d<=n:
		if n%d==0:
			Ans.append(d)
			n//=d
		else:
			d+=1
	if n>=1:
		Ans.append(n)
	return Ans

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

for i in range(2,1000000):
	mas=1
	k=set(Factor(i))
	for j in k:
		mas*=(j/(j-1))
	func[i]=mas
	
print(get_key(func, max(func.values())))
