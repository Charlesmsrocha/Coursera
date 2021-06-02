def multiplicartion_table(number):
    multiplier = 1

    while multiplier <= 5:
        result = multiplier * number
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplicartion_table(3)
multiplicartion_table(5)
multiplicartion_table(8)
