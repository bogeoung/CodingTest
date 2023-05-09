import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9) # timeout을 해결하기 위해서 추가 필요 

def input_func(N):
  arr = [[] for _ in range(N+1)]
  for _ in range(N-1):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
  
  dp = [[0,1] for _ in range(N+1)]
  visited = [0] * (N + 1)
  return arr, dp, visited

def dfs(cur_node):
  visited[cur_node] = 1
  for friend in arr[cur_node]:
    if visited[friend] == 0: # 방문한 적 없는 친구
      dfs(friend) # 가장 깊은 친구를 찾을때까지 dfs 호출
      dp[cur_node][0] += dp[friend][1] # 내가 얼리어답터가 아닌 경우, 내 친구는 무조건 얼리어답터이여야함. 
      dp[cur_node][1] += min(dp[friend][0], dp[friend][1]) # 내가 얼리어답터인 경우, 친구의 얼리어답터 여부는 상관 없기 때문에 min값 사용

def main():
  N = int(input())
  global arr
  global dp
  global visited
  arr, dp, visited = input_func(N)
  dfs(1)
  print(min(dp[1])) # 가장 부모 노드의 필요한 얼리어답터 수를 출력

if __name__ == "__main__":
  main()