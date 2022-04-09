from traceback import print_tb


numbers = range(1500, 2500)
for i in numbers:
    # if (i % 5) == 0:
    #     print(i)
    # elif(i % 7)==0:
    #     print(i)
    

    if (i % 5) ==0 and (i % 7) == 0:
        print(i)


#  was not sure which one the exercise ment so:
# 1. shows the numbers that can be devided to 5 with no remain plus the numbers that can be devided in seven with no remains.
# 2. shows only numbers that can be devided in 5 and 7 with no remains.
