class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_history = []
        for i in operations:
            if i.lstrip("-").isdigit():
                score_history.append(int(i))
            elif i == '+':
                score = score_history[-1] + score_history[-2]
                score_history.append(score)
            elif i == 'D':
                score = 2 * score_history[-1]
                score_history.append(score)
            elif i == 'C':
                score_history.pop()
        return sum(score_history)


