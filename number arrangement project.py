a =int(input("enter you number:"))

b = int(input("enter you number:"))

c = int(input("enter you number:"))

if(a>=b>=c ):
    print(int(a),int(b),int(c))

if( b>=a>=c):
    print(int(b),int(a),int(c))

if(c>=a>=b):
    print(int(c),int(a),int(b))

if(a>=c>=b):
    print(int(a),int(c),int(b))

if(b>=c>=a):
    print(int(b),int(c),int(a))

if(c>=b>=a):
    print(int(c),int(b),int(a))


num = [input("enter the no. :"), input("enter the no. :"), input("enter the no. : ")]
a = input("enter the order you want to sort in (asc/desc): ")
if(a=="asc"):
    num.sort()
    print(num)

if(a=="desc"):
    num.sort(reverse=True)
    print(num)
