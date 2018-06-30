a=float(input('number 1 : '))
b=float(input('number 2 : '))
print('select the operation : \n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.Exit')
ch=input('option : ')
while(ch!='5'):
    if ch=='1':
        add=a+b
        print(a,'+',b,'=',add)
    elif ch=='2':
        sub=a-b
        print(a,'-',b,'=',sub)
    elif ch=='3':
        mul=a*b
        print(a,'*',b,'=',mul)
    elif ch=='4':
        div=a/b
        print(a,'/',b,'=',div)
    else:
        print('select correct option')
    ch=input('option : ')
print('thank you')

