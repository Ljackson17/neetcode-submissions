class Solution:
    def checkValidString(self, s: str) -> bool:
        from collections import deque
        leftQueue = deque()
        starQueue = deque()
        for i in range(len(s)):
            if s[i] == '(':
                leftQueue.append(i)
            elif s[i] == '*':
                starQueue.append(i)
            else:
                if len(leftQueue) != 0:
                    leftQueue.pop()
                elif len(starQueue) != 0:
                    starQueue.pop()
                else: return False
        while leftQueue and starQueue:
            if leftQueue[-1] < starQueue[-1]:
                starQueue.pop()
                leftQueue.pop()
            else:
                break
        return not leftQueue

