# Constantes and global variables
TAG = '#'
SIGMA = 'I'
MARK = 'x'
CURSOR = '>'
WHITE = 'b'
tape2 = ''
tape1 = ''
head1 = 0  # cabeçote da fita 1
head2 = 0  # cabeçote da fita 2
list1 = []
list2 = []

# constants functions
def denied():
    print('REJEITA')

def accepted():
    print('ACEITA')

def printtapes():
    global list1, list2
    print(f'tape 1: {list1}')
    print(f'tape 2: {list2}')

def movecursortoright():
    global list1, list2, head1, head2
    if list1[head1] != WHITE:
        list1[head1] = CURSOR
        list1[head1 - 1] = SIGMA

def movecursortoleft():
    global list1, list2, head1, head2
    if list1[head1] != WHITE:
        list1[head1] = CURSOR
        list1[head1 + 1] = SIGMA

def printheads():
    global head1, head2
    print(head1)
    print(head2)
# functions states
def q0():
    global head1, head2, tape1, tape2, list1, list2
    printheads()
    list1[head1 + 1] = CURSOR
    list2[head2 + 1] = CURSOR
    print('q0')
    head1 += 1
    head2 += 1
    printtapes()
    q1()

def q1():
    global head1, head2, tape1, tape2, list1, list2
    print('q1')
    printheads()
    while list1[head1] != WHITE and list2[head2] != WHITE:
        head1 += 1
        head2 += 1
        printheads()
        movecursortoright()
        if list2[head2] != WHITE:
            list2[head2] = CURSOR
            list2[head2 - 1] = SIGMA
        printtapes()
    q3()

def q3():
    global head1, head2, tape1, tape2, list1, list2
    print('q3')
    printheads()
    while list1[head1] != WHITE:
        printheads()
        head1 -= 1
        movecursortoleft()
        printtapes()
    q18()

def q18():
    global head1, head2, tape1, tape2, list1, list2
    print('q18')
    while list1[head1] == SIGMA:
        head1 += 1
        printtapes()
    q16()

def q16():
    global head1, head2, tape1, tape2, list1, list2

def main():
    global tape1, tape2
    tape1 = input('').upper()
    tape1 = 'b' + tape1 + 'b'  # a letra b representa o branco na fita
    tape2 = tape1
    for x in tape1:
        list1.append(x)
    for y in tape2:
        list2.append(y)

    q0()


main()

