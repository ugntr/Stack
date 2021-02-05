import sys

def isempty(st):
    if st == []:
        return True
    else:
        return False

def stackinsert(st):
    item = input('Enter what you want to input:  ')
    st.append(item)
    print('Item added!!\n')


def peek(st):
    item = isempty(st)
    if item == True:
        print('Underflow!! \n')
    else:
        print(st[-1], '<- Top\n')

def show(st):
    item = isempty(st)
    if item == True:
        print('Underflow!!\n')
    else:
        if len(st) == 1:
            print(st[0], '<-Top, Bottom\n')
        else:
            print(st[-1], '<- Top')
            for i in range(len(st)-2, 0, -1):
                print(st[i])
            print(st[0], '<- Bottom\n')

def pop(st):
    item = isempty(st)
    if item == True:
        print('Underflow!!\n')
    else:
        to_pop = st[-1]
        st.pop(-1)
        print('Item POPPED!!\n')


stack_list = []

def ask():
    print('0:Quit, 1:insertion, 2:peek, 3:show, 4:pop')
    try:
        prompt = int(input('enter any of the given numbers:  '))
    
    except ValueError:
        print('Please enter the above given number!!\n')
        ask()

    if prompt == 0:
        sys.exit()

    elif prompt == 1:
        stackinsert(stack_list)
        ask()

    elif prompt == 2:
        peek(stack_list)
        ask()
    
    elif prompt == 3:
        show(stack_list)
        ask()

    elif prompt == 4:
        pop(stack_list)
        ask()

ask()

