# 최고의 집합


def solution(n, s):
    if n > s : 
        return [-1]
    else:
        num = s // n
        ran = s % n 
        if ran == 0:
            answer = [num for i in range(n)]
            return answer
        else:
            answer = [num for i in range(n)]
            answer[0:ran] = [num+1 for i in range(ran)]
            answer.reverse()
            return answer