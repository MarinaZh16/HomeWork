while 1:
    print('Enter the number:')
    a=int(input())
    if not a%2==0 and a%3==0:
        print('BINGO!!!', a)
    else:
        print('try again')
