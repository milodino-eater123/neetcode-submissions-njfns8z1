class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            for ltr in string:
                encoded_string += f"{ord(ltr)}"
                encoded_string += "S"
            encoded_string += 'N'
        return encoded_string


    def decode(self, s: str) -> List[str]:
        result = []
        string = ""
        ltr = ""
        for n in s:
            if n == "S":
                string += chr(int(ltr))
                ltr = ""
                continue
            elif n == "N":
                result.append(string)
                string = ""
                continue
            ltr += n
        return result



