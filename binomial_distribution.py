p=float(input("p : "))
q=float(input("q : "))
n=int(input('n : '))
if n==0 or n==1:
    fact=1
elif n<0:
    print('enter "n" as positive value')
else:
    fact=1
    for j in range(1,n+1):
        fact=fact*j
x=int(input('x : '))
if x==0 or x==1:
    facto=1
elif x<0:
    print('enter "x" as positive value')
else:
    facto=1
    for i in range(1,x+1):
        facto=facto*i

n1=n-x
if n1==0 or n1==1:
    factor=1
elif n1<0:
    print('enter "n-x" as positive value')
else:
    factor=1
    for k in range(1,n1+1):
        factor=factor*k
print('')

p1=fact
p2=facto
p3=factor
bino=(p1/(p2*p3))*(p**x)*(q**(n-x))
print("your binomial distribution =",bino)
