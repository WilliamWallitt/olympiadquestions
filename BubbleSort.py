# Bubble sort, compares next neighbour in turn
# Swapping them if they are out of sequence
# Goes through all the data

def bubble_sort():
    output = input("Enter Number here : ")
    output = str(output)
    unsorted_list = [int(x) for x in output]

    for i in range(0, len(unsorted_list) - 1):
        for j in range(0, len(unsorted_list) - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j + 1], unsorted_list[j]


    return unsorted_list

print(bubble_sort())