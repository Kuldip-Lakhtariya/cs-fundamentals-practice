# Pattern : Here we make a dictionary with close brackets, and an empty list. Then we first check the first element is in the paris,if yes means parantheses start with close bracket then flase, if not then append. When we have second element we check with its value with preciovs element, if match then pop otherwise false.
class Solution:
    def isValid(self, s:str) -> bool:
        pairs: dict[str,str] = {")":"(","[":"]","{":"}"}
        stack: list[str] = []

        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack