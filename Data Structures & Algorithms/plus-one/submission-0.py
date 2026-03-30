class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string =""
        #convert to number
        for n in digits:
            string += str(n)

        string = int(string) + 1 

        #convert back to list
        string = str(string)
        return list(string)
        