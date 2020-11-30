#dictionary method
def twosum(nums, target):
    h = {}

    for i, num in enumerate(nums):
        n = target - num

        if n not in h:
            h[num] = i

        else:
            return [h[n], i]

# Two sum II - two pointer method
# l = 0
# r = len(numbers) - 1
# while l < r:
#     s = numbers[l] + numbers[r]
#     if s == target:
#         return [l + 1, r + 1]
#     elif s > target:
#         r -= 1
#     else:
#         l += 1

nums = [2,7,11,15]
target = 9
res = twosum(nums, target)
print(res)