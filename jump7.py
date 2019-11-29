L = range(1,101)
for i in L:
    if i%7 == 0:
        continue
    elif i%10 == 7 or i//10 == 7:
        continue
    else:
        print(i)

