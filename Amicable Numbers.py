def amicable_numbers(first_number, second_number):
    total = 0
    total1 = 0
    for i in range(first_number + 1):
        if i != 0 and first_number % i == 0 and i != first_number:
            total += i
    for j in range(second_number + 1):
        if j != 0 and second_number % j == 0 and j != second_number:
            total1 += j

    if first_number == total1 and second_number == total and first_number != second_number:
        return "Amicable"
    else:
        return "Not Amicable"

print(amicable_numbers(2620, 2924))

x = [i + 1 for i in range(1000)]
counter = 1

while counter < 300:
    for number in x:
        if number == 1000:
            counter += 1
        if amicable_numbers(number, counter) == "Amicable":
            print(number, counter)




