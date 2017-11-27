import MarbleDefs

def solver(alist):
    alistsort = sorted(list(alist))

    while alist != alistsort
        if alist[0] == 0:
            rotate(alist)
            print alist, "Rotated"
        if alist[1] == 0:
            rotate(alist)
            print alist, "Rotated"
        if alist[0]>alist[1]:
            switch(alist)
            print alist, "Switched"
        if alist[1]>alist[0]:
            rotate(alist)
            print alist, "Rotated"
        else alist == alistsort: print "Complete!"
