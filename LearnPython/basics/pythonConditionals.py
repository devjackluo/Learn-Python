# if statement

x = 6
y = 9
z = 4
a = 2
b = 6

if x > y:
    print("x greater than y")
    if x > z:
        print('nest statement x > z')

if x < y:
    print("x less than y")
    if x > z:
        print('\tnest statement x > z')

print("")

# python can do multiple conditions at once... wtf

if z < y > x > a:
    print('y greather than z and greather than x and greather a && x greather than a')

a = 7

print("")

if z < y > x > a:
    print('y greather than z and greather than x and greather a && x greather than a')
else:
    print('something was not right, a became greather than x')

print("")

if b == a:
    print('b equals a')
elif b == z:
    print('b equals z')
elif b == y:
    print('b equals y')
elif b != x:
    print('b !equals x')
else:
    print('b not equal to anything above')
    if b == x:
        print('\tnested if: b equals x however')


print("")