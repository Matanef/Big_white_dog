list1 = [5, 10, 15, 20, 25, 50, 20]

print(list1)

index_twenty = list1.index(20)
print(index_twenty)

list1[index_twenty] = 200
print(list1)



list2 = [5, 10, 15, 20, 25, 50, 20]
# we can use a while loop to play with the list abit for example:
while 20 in list2:
    index_twenty = list2.index(20)
    list2[index_twenty] = 200

print(list2)

# althought htis is not according to the exercise we wrote a loop that will switch all "20" in the list to "200".
 