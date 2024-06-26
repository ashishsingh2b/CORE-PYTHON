i = 0

def myfunc():
    global i
    i = i+1
    print("i")
    myfunc()

myfunc()
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())