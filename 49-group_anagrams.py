class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in range(len(strs)):
            sortValue = str(sorted(strs[i]))
            if sortValue in hmap:
                hmap[sortValue].append(strs[i])

            else:
                hmap[sortValue] = [strs[i]]

        return [v for k,v in hmap.items()]


            



        