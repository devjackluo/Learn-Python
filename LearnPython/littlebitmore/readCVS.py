import csv

with open('exampleCSV.csv') as csvfile:

    # delimiter tells what regex to cut at
    readCSV = csv.reader(csvfile, delimiter=',')

    dates = []
    colors = []

    print(readCSV)

    for row in readCSV:
        #print(row)
        #print(row[0],row[-1])
        color = row[-1]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    whatColor = input("what color do you wish to know the date of? : ")

    try:

        if whatColor in colors:
            colorIndex = colors.index(whatColor.lower())
            theDate = dates[colorIndex]
            print('the date of',whatColor,'is',theDate)
        else:
            print(whatColor,"not found")

    except Exception as e:

        print(whatColor,"not found -- Exception:",e)



print('''

jack
is
awesome
we
print multiline

in ruby, we call this heredoc?

''')