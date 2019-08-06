while True:
    print("enter 'q' to quit.")
    number_1 = input("please enter the first number: ")
    if number_1 == "q":
        break
    number_2 = input("please enter the second number: ")
    if number_2 == "q":
        break

    try:
        number = int(number_1) + int(number_2)
    except ValueError:
        print("maybe one of your number provided is not a number type")
    else:
        print(number)