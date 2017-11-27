import random
import MarbleDefs
import solver

listlength = input("Enter list length:")
listlength = int(listlength)
list1 = random.sample(range(listlength), listlength)

list1sort = sorted(list(list1))
print list1, "Your starting list."

if list1 == list1sort:
    print "Your list is already sorted."
else: solver(list1)

# This will run at an n log n timeframe.  This will be longer than a linear
# timeframe, since each digit can be switched or rotated several times during
# run.  This will not increase beyond n log n, since this will not be a
# polynomial (squared, or other increased power).
