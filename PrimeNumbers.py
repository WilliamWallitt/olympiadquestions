# For each number divide it by itself
# And numbers below it
# If any division that isnt 1 or itself
# Gives remainder = 0, not a prime

def prime_number(max_num):
    if max_num >= 2:
        print('2')
    for number in range(max_num):
        number += 1
        for division in range(number):
            division += 1
            if division == 1:
                continue
            elif division == number or max_num == number:
                break
            else:
                if number % division == 0:
                    break
                elif division == number - 1:
                    print(number)
                    break

prime_number(100)






