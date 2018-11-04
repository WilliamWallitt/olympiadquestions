def digital_river(n):
    if n < 0 or n > 16384:
        return "Invalid n number"

    total = 0
    n = str(n)
    for i in n:
        i = int(i)
        total += i
    total += int(n)

    return total

n = 140
list = [n]
list1 = []
list3 = []
list9 = []
n1 = 1
n3 = 3
n9 = 9
for i in range(100):

    new = digital_river(n)
    list.append(new)
    test1 = digital_river(n1)
    test3 = digital_river(n3)
    test9 = digital_river(n9)
    list1.append(test1)
    list3.append(test3)
    list9.append(test9)
    n1 = test1
    n3 = test3
    n9 = test9
    n = new

counter = 0
for i in list:
    counter += 1
    if i in list1:
        print("First meets river 1 at", i)
        break
    elif i in list3:
        print("First meets river 3 at", i)
        break
    elif i in list9:
        print("First meets river 9 at", i)
        break
    else:
        if counter == len(list):
            print("No Crosses")










