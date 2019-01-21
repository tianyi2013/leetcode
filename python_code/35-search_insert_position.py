def search_insert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums or target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    else:
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif num < target:
                if i + 1 < len(nums) and target < nums[i + 1]:
                    return i + 1


def search_insert_binary(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = (j + i) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            i = mid + 1
        else:
            j = mid - 1
    return i


print(search_insert_binary([1], 0))
