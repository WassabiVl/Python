import time
start_time = time.time()


def myShortBubbleSort(aList):
    exchanges = True
    passNum = (len(aList) - 1)
    x = 0
    while passNum > 0 and exchanges:
        exchanges = False
        for i in range(x, passNum):
            if aList[i] > aList[i + 1]:
                exchanges = True
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp
    for i in range(passNum - 1, x, -1):
        if aList[i] > aList[i + 1]:
            exchanges = True
            temp = aList[i + 1]
            aList[i + 1] = aList[i]
            aList[i] = temp
        x += 1
        passNum = passNum - 1


alist1 = [93, 54, 26, 62, 17, 77, 31, 44, 55, 20, 10]
myShortBubbleSort(alist1)
print(alist1)
print("--- %s seconds ---" % (time.time() - start_time))
#  steps taken 305, time 0.11028528213500977 seconds
#  if the second if statment is implemented in the first, it becomes insertion sort