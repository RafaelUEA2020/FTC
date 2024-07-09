# Rafael Santos e Gustavo Almada
# Constantes and global variables
TAG = '#'
SIGMA = 'I'
MARK = 'x'
WHITE = 'b'
ACEITA = 'ACEITA'
REJEITA = 'REJEITA'
tape2 = ''
tape1 = ''
head1 = 1  # cabeçote da fita 1
head2 = 1  # cabeçote da fita 2
list1 = []
list2 = []

def printtapes():
    global list1, list2
    print(f'tape 1: {list1}')
    print(f'tape 2: {list2}')

def q0():
    global list1, list2, head1, head2
    if list1[head1] == TAG:
        print(REJEITA)
    else:
        head1 += 1
        head2 += 1
        q1()

def q1():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == TAG:
            head1 += 1
            q2()
            break
        head1 += 1
        head2 += 1

def q2():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == WHITE:
            head1 = head1 - 1
            q3()
            break
        head1 += 1
        head2 += 1

def q3():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == TAG:
            head1 = head1 - 1
            q18()
            break
        head1 = head1 - 1

def q18():
    global list1, list2, head1, head2
    if list1[head1] == SIGMA:
        head1 += 1
        q16()
    elif list1[head1] == MARK:
        head1 += 1
        q17()
    elif list1[head1] == TAG:
        print(list1[head1])
        print(head1)
        print(REJEITA)

def q17():
    global list1, list2, head1, head2
    head1 += 1
    list2[head2] = '='
    head2 += 1
    q20()

def q20():
    global list1, list2, head1, head2
    list1[head1] = WHITE
    head1 += 1
    q21()

def q21():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == WHITE:
            head1 -= 1
            q30()
            break
        head1 += 1

def q30():
    global list1, list2, head1, head2, tape2
    while True:
        if list1[head1] == TAG:
            list1[head1] = SIGMA
            tape2 = tape2 + SIGMA
            head1 -= 1
            q31()
            break
        head1 -= 1

def q31():
    global list1, list2, head1, head2, tape2
    tape2 = tape2 + '='
    while True:
        head1 -= 1
        if list1[head1] == MARK:
            list1[head1] = SIGMA
            tape2 = tape2 + SIGMA
        if list1[head1] == WHITE:
            head1 += 1
            q23()
            break


def q23():
    global list1, list2, head1, head2, tape2
    while True:
        if list1[head1] == WHITE:
            q24()
            break
        list1[head1] = WHITE
        head1 += 1

def q24():
    global list1, list2, head1, head2, tape2
    print(tape2 + ' ' + ACEITA)

def q16():
    global list1, list2, head1, head2
    head1 += 1
    q4()

def q4():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == WHITE:
            head1 -= 1
            q10()
            break
        elif list1[head1] == SIGMA:
            list1[head1] = TAG
            head1 += 1
            q5()
            break
        head1 += 1

def q5():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == WHITE:
            head1 -= 1
            q6()
            break
        head1 -= 1

def q6():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == TAG:
            q7()
            head1 -= 1
            break
        head1 -= 1

def q7():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == WHITE:
            q8()
            head1 += 1
            break
        head1 -= 1

def q8():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == SIGMA:
            list1[head1] = TAG
            head1 += 1
            q9()
            break
        head1 += 1

def q9():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == TAG:
            head1 += 1
            q3()
            break
        elif list1[head1] == WHITE:
            head1 -= 1
            q3()
            break
        head1 += 1

def q10():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == TAG:
            head1 += 1
            q11()
            break
        head1 -= 1

def q11():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == WHITE:
            head1 -= 1
            q12()
            break
        elif list1[head1] == TAG:
            q3()
            break
        head1 -= 1

def q12():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == MARK:
            list1[head1] = SIGMA
            head1 -= 1
            q13()
            break
        head1 -= 1

def q13():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == TAG:
            head1 -= 1
            q14()
            break
        head1 -= 1

def q14():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == WHITE:
            head1 += 1
            q15()
            break
        head1 -= 1

def q15():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == TAG:
            list1[head1] = SIGMA
            head1 += 1
            q19()
            break

def q19():
    global list1, list2, head1, head2
    while True:
        if list1[head1] == TAG:
            head1 += 1
            q11()
            break
        head1 += 1

def main():
    global tape1, tape2, list1, list2, head1, head2
    tape1 = input('').upper()
    tape1 = 'b' + tape1 + 'b'  # a letra b representa o branco na fita
    print(tape1)
    tape2 = tape1
    for x in tape1:
        list1.append(x)
    for y in tape2:
        list2.append(y)
    if TAG not in list1:
        print(REJEITA)
    else:
        q0()


main()
