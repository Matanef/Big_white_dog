import random
nums = None
def getnums(n):
    global nums
    nums = [random.randint(1,n//d) for x in range(n)]

def longest_sequence(nums: list) -> int:
    longest_streak = 0
    for num in nums:
        current_num = num
        current_streak = 1
        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1
        longest_streak = max(longest_streak, current_streak)
    return longest_streak

