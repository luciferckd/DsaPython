
def Linear_sear(array , target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

super = Linear_sear([19, 34, 68, 90, 834], 34)
print(super)