list = ['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'final']
length = int(len(list))
for i in range(1, length, 2):
    print(list[i])


    # ok, finally so this is i in range of (starting point = position 1 translate to 'second', length of the list as stored in length variable, and we declare step size of the loop = 2)