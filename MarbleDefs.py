
#Here is the function that switches the first and second position:
def switch(alist):
    alist[0], alist[1] = alist[1], alist[0]
    return alist

#Here is the function that moves the first position to the last:
def rotate(alist):
    temp = [alist[0]]
    alisttemp = alist + temp
    del alisttemp[0]
    alist = alisttemp
    return alist
