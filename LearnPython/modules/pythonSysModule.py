import sys
from subprocess import call

#sys.stderr.write('This is stderr text\n')
#sys.stderr.flush()
#sys.stdout.write("this is stdout text\n")

#print(sys.argv)


def main(arg):
    print(arg)

main(sys.argv[1])

'''
if len(sys.argv) > 1:
    # call this in cmd --  python pythonSysModule.py 'ruby main_puzzle_luo.rb'
    call(sys.argv[1])
'''
