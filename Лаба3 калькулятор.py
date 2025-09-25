while (True):
    print("выбор действий ")
    print( "1. +, -, *, /, **", "2. вывод из под корня", "3. решение квадратного уравнения", sep="\n" )
    выбор = input("действие ")

    match выбор:
        case "1":
            op = input("выбор операции")
            number1 = float(input("введите первое число"))
            number2 = float(input("введите второе число"))

            match op:
                case "+":
                    print(number1 + number2)
                case "-":
                    print(number1 - number2)
                case "*":
                    print(number1 * number2)
                case "/":
                    if  number2 != 0:
                        print(number1 / number2)
                    else:
                        print("ошибка деления на ноль")
                case "**":
                    print(number1 ** number2)
                case "%":
                    print(number1 % number2)
        case "2":
            koren = float(input("число для вывода из корня"))
            sqrt = float(input("введите степень корня"))

            if koren >= 0:
                print(pow(koren, (1/sqrt)))
            else:
                print("ошибка, корень меньше 0")
        case "3":
            a = float(input("коэффициент 'a': "))
            b = float(input("коэффициент 'b': "))
            c = float(input("коэффициент 'c': "))
            if a!=0:
                D = b** 2-4*a*c
                if D>0:
                    x1 = (-b + pow(D,0.5))/(2*a)
                    x2 = (-b - pow(D,0.5))/(2*a)
                    print("равные корни: ",x1,x2)
                elif D==0:
                    x = -b / (2*a)
                    print(x)
                else:
                    print("недействительные корни")
            else:
                print("ошибка")
        case _:
            print("ошибка")





