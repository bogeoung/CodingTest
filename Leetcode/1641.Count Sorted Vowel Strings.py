class Solution:
    def countVowelStrings(self, n: int) -> int:
        # 초기 배열 설정
        answer = [1, 1, 1, 1, 1]

        # n이 1인 경우 바로 반환
        if n == 1:
            return 5

        # 2부터 n까지 반복
        for _ in range(1, n):
            for i in range(1, 5):
                answer[i] += answer[i - 1]

        # 가능한 문자열의 수는 배열의 모든 요소의 합
        return sum(answer)
