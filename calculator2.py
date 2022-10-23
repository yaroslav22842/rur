symbol = ""
war = "false"

while symbol != "0":

    if symbol != "5":
        stroke1 = input("введите первое число: ")
        stroke2 = input("введите второе число: ")
    if symbol == "5":
        stroke = input("Какой ряд хочеш заменить?")
        number = input("На какое число хочеш заменить?")
        if stroke == ("1"):
            stroke1 = (f"{number}")
        elif stroke == ("2"):
            stroke2 = (f"{number}")

    print("1 = +")
    print("2 = -")
    print("3 = /")
    print("4 = *")
    print("5 = замена числа")
    print("0 = выход")
    symbol = input("введите номер действия: ")





    if symbol != "1" and symbol != "2" and symbol != "3" and symbol != "4" and symbol != "5" :
     print("error")

    else:
       print("проверка закончена успешно")
    if symbol==("2"):
        answer=(float(stroke1)-float(stroke2))
        sus = ("-")
    if symbol==("1"):
        answer=(float(stroke1)+float(stroke2))
        sus = ("+")
    if symbol==("3"):
        answer=(float(stroke1)/float(stroke2))
        sus = ("/")
    if symbol==("4"):
        answer=(float(stroke1)*float(stroke2))
        sus = "*"
    if symbol==("5"):

           continue

    full = (f"{stroke1}{sus}{stroke2}={answer}")


    print("Напишите 123>>")

    if input() == "123":
     print(f"{full}")
     print("----------------")
    else:
     print("неправильно")
