
exec("print('hello there')")

list_str = "[3,5,1,5,1,5,14]"
list_str = exec(list_str)     #list_str = execution of list = None
print(list_str)

exec("list_str2 = [35,35,25,2352,5]")
print(list_str2)

exec("def test(): print('oooohhhh snappp!!')")
test()

exec('''
def test2():
    print('multiple lane?? oh snappp1!!')
''')

test2()

