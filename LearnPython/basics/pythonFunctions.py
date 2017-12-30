
# basic function

def example():
    print('example function called')
    z = 30 / 9
    print(z)


example()

print("")






# parameters

def simpleAddition(num1, num2):
    print("simple addtion function called")
    answer = num1 + num2
    print(num1)
    print(num2)
    print(answer)
    if answer > 5:
        print('\tanswer is greater than 5')


simpleAddition(9, 10)
print("")
# python you can do this syntax to not order them
simpleAddition(num2=100, num1=6)







# default parameters

print('')

def multiByFive(num1, num2=5):
    print("multi by 5 called")
    answer = num1 * num2
    print(answer)

multiByFive(5)
# you can override default
multiByFive(5, 100)

print('')


def basicWindow(width, height, font="Times New Roman", bgc="White", scrollBar=True):
    print(f"width: {width} height:{height} font:{font} backgroundColor:{bgc}")

basicWindow(500, 500)
# if you only want to change bgc
basicWindow(500, 500, bgc="Black")
