#This is bubble sort method i think
p = str(input("Sıralamak istediğin sayıları  boşluk bırakarak gir: "))

nums = []

for j in p.split():
    nums.append(int(j))

for x in range(len(nums)):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i +1]:
            nums[i],nums[i +1] = nums[i +1],nums[i]

print(nums)
