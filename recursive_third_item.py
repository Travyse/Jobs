def third_item(nums=[]):
    if len(nums) >= 3:
        print(nums[2])
        third_item(nums[3:])
