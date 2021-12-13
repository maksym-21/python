# Napisać iteracyjną wersję funkcji quicksort()
# iterative version of quicksort with the help of an auxiliary stack


def partition(array, low, high) :
    element = array[high]
    index = low - 1

    for j in range(low,high) :
        if array[j] <= element :
            index += 1
            array[index], array[j] = array[j], array[index]

    array[index + 1] , array[high] = array[high], array[index + 1]
    return index + 1

def quick_sort(array, low, high) :
    stack = [0] * (high - low + 1)
    top = -1

    # pushing into stack
    top += 1
    stack[top] = low

    top += 1
    stack[top] = high

    while top >= 0 :
        # popping from stack
        high1 = stack[top]
        top -= 1

        low1 = stack[top]
        top -= 1

        # pivot element
        pivot = partition(array, low1, high1)

        # if elements on right side of pivot -> push right side into stack
        if pivot + 1 < high1 :
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = high1
        # if elements on left side of pivot -> push left side into stack
        if pivot - 1 > low1 :
            top += 1
            stack[top] = low1
            top += 1
            stack[top] = pivot - 1


array = [19, 13, 5, 2, 1, 7]
quick_sort(array, 0, len(array) - 1)

print ("Sorted array is -> " + array.__str__())






