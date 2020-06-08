"""
Given a non-empty array of integers, return the k most frequent elements.
"""

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def partition(left, right, pivot):
        pivot_freq = counter[unique[pivot]]
        unique[pivot], unique[right] = unique[right], unique[pivot]

        store_index = left

        for i in range(left, right):
            if counter[unique[i]] < pivot_freq:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1
        unique[right], unique[store_index] = unique[store_index], unique[right]
        return store_index

    def quick_select(left, right, smallest):
        if left == right: return

        pivot = random.randint(left, right)
        pivot = partition(left, right, pivot)

        if smallest == pivot:
            return
        elif smallest <  pivot:
            quick_select(left, pivot-1, smallest)
        else:
            quick_select(pivot+1, right, smallest)

    counter = Counter(nums)
    unique =  list(counter.keys())
    n = len(unique)
    quick_select(0, n-1, n-k)
    return unique[n-k:]



