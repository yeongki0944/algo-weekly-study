class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        num = 0
        for n in digits:
            num = num * 10 + n
        num += 1
        for c in str(num):
            answer.append(c)
        return answer