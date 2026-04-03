class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #buckt sort
        #first, create a hash map that stores every value as keys and 
        #their frequencies as values

        #Then create a freq array, indice is the frequency of that number
        #put the number/numbers under corresponding indice(frequency)

        #loop from last indice to the beginning of the freq array,
        #append top k elements into result array.
        #Note, each indice in freq array may has a list whose length greater than 1,
        #make sure loop every element in the target list.
        
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freq = [[]for _ in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

