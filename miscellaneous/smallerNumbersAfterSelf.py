'''
You are given an integer array nums and you have to return a new
counts array. The counts array has the property where counts[i] 
is the number of smaller elements to the right of nums[i].
'''

def countSmaller(nums: List[int]) -> List[int]:
    out = []
    for i in range(len(nums)):
        count = 0
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                count += 1
        out.append(count)
    return out


def countSmaller(nums: List[int]) -> List[int]:
    out = []
    nums_tuple = [(num, i) for i, num in enumerate(nums)]
    sorted_nums = sorted(nums_tuple, key = lambda l:l[0])

    def binary_search(x, idx):
        l, r = 0, len(sorted_nums)-1
        while l <= r:
            mid = (l + r)//2
            if sorted_nums[mid][0] == x:
                if sorted_nums[mid][1] == idx:
                    return sorted_nums[mid], mid
                else:
                    if mid > 0 and sorted_nums[mid-1][0] == x and sorted_nums[mid-1][1] <= idx:
                        j = mid
                        while sorted_nums[j][0] == x:
                            j -= 1
                        return sorted_nums[j+1], j+1

                    else:
                        j = mid
                        while j < len(sorted_nums) and sorted_nums[j][0] == x:
                            j += 1
                        return sorted_nums[j-1], j-1

            elif sorted_nums[mid][0] < x:
                l = mid + 1
            else:
                r = mid - 1

    for idx, num in enumerate(nums):
        pair, mid = binary_search(num, idx)
        count = 0
        for i in range(mid):
            if sorted_nums[i][1] > pair[1]:
                count += 1
        out.append(count)
    return out


def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        result = collections.deque() 
        for i in range(len(nums)-1,-1,-1):
            idx = bisect.bisect_left(arr, nums[i])
            result.appendleft(idx)
            arr.insert(idx, nums[i])
        return result
