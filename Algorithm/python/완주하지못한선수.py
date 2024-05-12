# 완주하지 못한 선수
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant.sort()
    completion.sort() 

    for p, c in zip(participant, completion):
        if p != c:
            return p
        else:
            return participant[-1]
