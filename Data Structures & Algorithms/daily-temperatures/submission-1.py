class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        output = [0] * len(temperatures) 

        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stackInd = stack.pop()
                output[stackInd] = (i - stackInd)
            stack.append(i)
        return output


        