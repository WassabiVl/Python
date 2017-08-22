import time
start_time = time.time()
def myShortBubbleSort(alist):
    exchanges = True
    passnum = (len(alist)-1)	
    x=0
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(x,passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       for i in range(passnum-1,x,-1):
	       if alist[i]>alist[i+1]:
	           exchanges = True
	           temp = alist[i+1]
	           alist[i+1] = alist[i]
	           alist[i] = temp
       x+=1
       passnum = passnum-1
	   
alist=[93,54,26,62,17,77,31,44,55,20,10]
myShortBubbleSort(alist)
print(alist)
print("--- %s seconds ---" % (time.time() - start_time))
#steps taken 305, time 0.11028528213500977 seconds
#if the second if statment is implemented in the first, it becomes insertion sort