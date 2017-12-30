from basics import secondClass


class NumberMod:

    def __init__(self):
        self.num = 0

    def setDefault(self, x):
        self.num = x

    def addition(self, y):
        self.num = self.num + y
        print(self.num)

    def subtraction(self, y):
        self.num = self.num - y
        print(self.num)

    def multiplication(self, y):
        self.num = self.num * y
        print(self.num)

    def division(self, y):
        self.num = self.num / y
        print(self.num)


numMod = NumberMod()
numMod.setDefault(10)
numMod.multiplication(5)
numMod.multiplication(10)
numMod.addition(3)
numMod.subtraction(100)
numMod.division(3)



# call the imported module? file? class

newClass = secondClass.importedClass()
newClass.calledImportFunction()