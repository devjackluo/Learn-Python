
# write

text = 'Sample Text to Save\nNewLine!'
saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()



# append

appendMe = "\nNew bit of information"
appendFile = open('exampleFile.txt', 'a')
appendFile.write(appendMe)
appendFile.close()



# read

readMe = open('exampleFile.txt', 'r').readlines()
print(readMe)