class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        sum_list = [0 for _ in range(n + 1)]

        for f, t, l in bookings:
            sum_list[f - 1] += l
            sum_list[t] += -(l)

        # print("sum_list : ", sum_list)
        answer = []
        cur_sum = 0
        for s in sum_list:
            cur_sum += s
            answer.append(cur_sum)

        # print(answer[:n])
        return answer[:n]
