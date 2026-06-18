class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return list(result.values())

O(n*m)    #as number of input (strings) grows, inner loop (characters in strings) stays the same 
O(n*m)    #n - need extra memory for each input. m - inputs are strings, amount of memory depends on how long string is
