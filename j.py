n=int(input())
o=0
for i in range(2,int(n/2)):
    if(n%i==0):
        o=1
k=str(n)
n=k[::-1]
n=int(k)
for i in range(2,int(n/2)):
    if(n%i==0):
         o=1
if(o==0):
    print("prime")
else:
    print("not prime")
