def subsetsum(numbers , target):
    check_for_numbers = {}
    for num in numbers:
        if (target - num) in check_for_numbers:
            print(f"True {num} + {(target - num)} = {target}")
            return True
        else:
            check_for_numbers[num] = True
    
    print(f"False {target}")
    return False


numbers = [12, -7, 20, 1, 4, -10, -1]
subsetsum(numbers,5)
subsetsum(numbers,89)
subsetsum(numbers,1)
subsetsum(numbers,11)