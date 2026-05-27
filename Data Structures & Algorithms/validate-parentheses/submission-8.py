class Solution:
    def isValid(self, s: str) -> bool:
        new = []
        opening = {"(", "[", "{"}       # set
        closing = {")", "]", "}"}       # set
        for i in s:
            if len(new) == 0 and i in closing:
                return False
            if i in closing:
                top = new[-1]
                if i == ")" and top != "(":
                    return False
                if i == "]" and top != "[":
                    return False
                if i == "}" and top != "{":
                    return False
                new.pop()
            if i in opening:
                new.append(i)
        return len(new) == 0