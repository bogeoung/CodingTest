def input_func():
    S = list(input())
    T = list(input())
    return S, T

def edit_string(arr):
    if arr[-1] == 'A':
        arr.pop()
    elif arr[-1] == 'B':
        arr.pop()
        arr.reverse()
    return arr


def solution(S,T):
    while(len(T) > len(S)):
        T = edit_string(T)
    if S == T:
        print("1")
    else:
        print("0")

def main():
    S, T = input_func()
    solution(S,T)

if __name__ == '__main__':
    main()