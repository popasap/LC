class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for i in s:
            if i in ["(", "[", "{"]:
                brackets.append(i)
            elif i == ")":
                if len(brackets) < 1:
                    return False
                elif brackets.pop() == "(":
                    continue
                else:
                    return False
            elif i == "]":
                if len(brackets) < 1:
                    return False
                elif brackets.pop() == "[":
                    continue
                else:
                    return False
            elif i == "}":
                if len(brackets) < 1:
                    return False
                elif brackets.pop() == "{":
                    continue
                else:
                    return False
        if len(brackets) >= 1:
            return False
        else:
            return True
