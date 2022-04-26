def doubleExist(num, arr, l, index):
    double = False
    for i in range(l):

        if num == arr[i] and i != index:
            double = True
            break

    return double

arr = [-2,0,10,-19,4,6,-8]
l = len(arr)

out = False

for i in range(l):

    num = arr[i]*2

    if doubleExist(num, arr, l, i) == True:
        out = True
        break

print(out)




