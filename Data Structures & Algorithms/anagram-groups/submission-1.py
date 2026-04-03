class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Basically, we need to find all anagram words
        #every anagram goes into a list
        #the list should be values of a dict
        #the key is an array that stores the information of how many times each letter appears in that word

        #to implement this, first we create a dict
        #then we create an id for every word in the given array
        #by creating a list contains 26 elements, default as 0
        #the indice of every 0 represent the indice of letter on alphabet
        #e.g., a is 0, b is 1 etc

        #Then this id serve as keys of the dict

        #finally, we return an list, contains sublist, which is the values of the dict

        #Note: list cannot be set as key, it must turn into a tuple.
        #When we initiate the default dictionary, we need to set every element as a list
        #dict = defaultdict(list), so that we can append anagram into it as a sublist.
        
        dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            dict[tuple(count)].append(s)
        
        return list(dict.values())