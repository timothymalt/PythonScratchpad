class MarblesBoard:
#Here is the function that switches the first and second position:
    def switch(alist):
        alist[0], alist[1] = alist[1], alist[0]
        print alist

#Here is the function that moves the first position to the last:
    def rotate(alist):
        firsti = [alist[0]]
        del alist[0]
        alisttemp = alist + firsti
        alist = alisttemp
        print alist

# This creates a randomized list, which is the initial
# input of the MarblesBoard game.

    import random
    listlength = input("Enter list length:")
    listlength = int(listlength)
    alist = random.sample(range(listlength), listlength)
    if alist == sorted(alist):
        print "You're list is sorted already."
    print alist

rotate(alist)
switch(alist)
