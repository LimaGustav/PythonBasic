nums = [0, 1, 5, 8, 7]

# Usando Index
for i in range(len(nums)):
    print(nums[i])

# Foreach
print("#"*20)
for n in nums:
    print(n)

# Index e valor
print("#"*20)
for i, n in enumerate(nums):
    print(i, n)


nums.sort(reverse=True)
print(nums)
