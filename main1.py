n=int(input("enter a number"))
p=n**(1/2)
for i in range(2):
	m=n/p
if(m==p):
	print("yes, given no is perfect squre")
else:
	print("not a squre")
