while 1:
    print('Enter the first number from 0 to 100 inclusive:')
    a=int(input())
    if a>100:
        print('''%s is not 'to 100 inclusive' ! Think harder !!!''')
    if a>90:
        print('You almost there')
    elif 10<a<90 and not a%2==0 and not a%7==0:
          print('BINGO!!!', a)
    else:
        print('try again')

        
          
