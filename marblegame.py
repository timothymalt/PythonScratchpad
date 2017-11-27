
#Here is the function that switches the first and second position:
def switch(alist):
    alist[0], alist[1] = alist[1], alist[0]
    print "switch result", alist

#Here is the function that moves the first position to the last:
def rotate(alist):
    temp = [alist[0]]
    alisttemp = alist + temp
    del alisttemp[0]
    alist = alisttemp
    print "rotate result", alist



import random
listlength = input("Enter list length:")
listlength = int(listlength)
list1 = random.sample(range(listlength), listlength)
print(list1)

switch(list1)
rotate(list1)
