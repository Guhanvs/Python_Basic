def largest_number(nums):
    largest=nums[0]
    for num in nums:
        if num>largest:
            largest =num
    return largest
print(largest_number([1,2,3,4,5,6,7,8,9]))