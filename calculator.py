num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
arith_arg = input('Что с ними делать? (+ для сложения, - для вычитания, * для умножения, / для деления, % для выделения целого остатка): ')
if arith_arg == '+':
    final = num1+num2
    print('Ответ: '+str(final))
elif arith_arg == '-':
    final = num1-num2
    print('Ответ: '+str(final))
elif arith_arg == '*':
    final = num1*num2
    print('Ответ: '+str(final))
elif arith_arg == '/':
    final = num1/num2
    print('Ответ: '+str(final))
elif arith_arg == '%':
    final = num1%num2
    print('Ответ: '+str(final))
else:
    print('Неизвестная операция')
xcxc=input('Enter для выхода')
