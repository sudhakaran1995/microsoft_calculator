x=5
y=4
z=5


def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

a=add(x,y,z)
print(a)
print('this is an addition function')
