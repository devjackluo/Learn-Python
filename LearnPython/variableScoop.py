
x = 6

def addToX(num):
    '''
    print(x)
    print(x+5)
    x += 6
    '''

    '''
    global x
    print(x)
    x += 6
    print(x)
    '''

    globx = x
    globx += num

    return globx

print('x is unchanged')
print(x)
print('call function to return value for x to be converted into')
x = addToX(100)
print(x)