# Brute force O(k*n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1

            else:
                hashMap[num] += 1
        ans = []
        for i in range(k):
            largest = 0
            key_larg = 0
            for k, v in hashMap.items():
                if v > largest:
                    largest = v
                    key_larg = k

            ans.append(key_larg)
            hashMap.pop(key_larg)
        return ans
