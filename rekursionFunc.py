i = 0

def f():
    global i
    i += 1
    f()

f()