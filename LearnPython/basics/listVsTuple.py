
# tuple - immutable
x = 3,2,4,5
x = (3,4,63,3)

# list
y = [3,5,2,5]


def exampleFunc():
    return (5,4,6),(6,35,2,5,6)

x,y = exampleFunc()

print(x)
print(y)


print(x[1],x[2])
print(y[2],y[3])






## List manipulation
print('\nlist stuff below')

x = [5,35,2,5,111,111]
x.append(2)
print(x)
x.insert(2, 666)
print(x)
x.remove(5)
x.remove(5)
#x.remove(5)
print(x)
x.pop(-1)
print(x)

# all element from 0 - 1 stop 2
print(x[0:2])
# get last element
print(x[-1])
# what index the element is at, first if multiple of same
print(x.index(111))
# count how many of these elements there are
print(x.count(111))


x.sort()
print(x)

# can't sort mixed values
# names = ["zach", 'bob', 'noah', 'alice', 1, 3, 335235, 23, 4]
names = ["zach", 'bob', 'noah', 'alice']
names.sort()
print(names)

# can have mixed list however
# maybe create module or function to sortMixList
mixList = ["zach", 'bob', 'noah', 'alice', 1, 3, 335235, 23, 4]
print(mixList)


