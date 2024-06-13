class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        for i in range(1,numRows+1):
            temp = [1 for _ in range(i)]
            print(temp)
            answer.append(temp)

        for i in range(numRows):
            for j in range(len(answer[i])):
                if j == 0 or j == len(answer[i]) - 1:
                    continue
                else:
                    answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
        return answer