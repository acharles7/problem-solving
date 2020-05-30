# Given 2 strings pin and guess. Write a function to provide a hint that indicates how digits in guess match the pin. Use:
# * - to indicate a number in the correct possition.
# o - to indicate that a number is present in the pin code but in a different possition.
# _ - to indicate that there's no such number in the pin code.


def pincodeGuess(pin, guess):
    output = ""
    pin_dic = {}
    guess_dic = {}
    for i in pin:
        pin_dic[i] = pin_dic.get(i, 0) + 1
    for i in guess:
        guess_dic[i] = guess_dic.get(i, 0) + 1
    # print(pin_dic)
    # print(guess_dic)
    pin_list = []
    guess_list = []
    for i in pin:
        pin_list.append(i)
    for i in guess:
        guess_list.append(i)

    n = len(pin)
    for i in range(len(pin_list)):
        if pin_list[i] == guess_list[i]:
            output += "*"
            # del pin_list[i]
            # del guess_list[i]

        elif pin_list[i] != guess_list[i]:
            if guess_list[i] in pin_list:
                output += "o"
            else:
                output += "_"
        print(pin_list)
        print(guess_list)

    print(output)


pin = "1234"
guess = "1224"

pincodeGuess(pin, guess)
