abc = input('Enter input string') + '$'
ptr = 0

def E():
    print("E")
    T()
    E1()

def E1():
    print("E1")
    global abc, ptr
    if abc[ptr] == '+':
        ptr += 1
        T()
        E1()
    else:
        return

def T():
    print("T")
    F()
    T1()

def T1():
    print("T1")
    global abc, ptr
    if abc[ptr] == '*':
        ptr += 1
        F()
        T1()
    else:
        return
def F():
    print("F")
    global abc, ptr
    if abc[ptr] == '(':
        ptr += 1
        E()
        if abc[ptr] == ')':
            ptr += 1
        else:
            print('Error')
            exit()
    elif abc[ptr] == 'a':
            ptr += 1
    else:
        print('Error')
        exit()

E()
if abc[ptr] == '$':
    print('Valid')
else:
    print('Invalid')

