
exDict = {'Jack':[23, 'blond'], 'Bob': [15, 'brown'], 'Alice':[12, 'black'], 'Kevin': [7,'red']}

print(exDict)
print("jack is",exDict['Jack'])
print("jack's hair color is",exDict['Jack'][1])

#add tim and change tim age
exDict['Tim'] = 14
print(exDict)
exDict['Tim'] = 67
print(exDict)

#kill tim
del exDict['Tim']
print(exDict)

