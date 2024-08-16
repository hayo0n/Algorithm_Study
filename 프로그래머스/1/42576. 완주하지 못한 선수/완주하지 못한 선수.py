def solution(participant, completion):
    dict = {}
    for i in participant:
        if i in dict:
            dict[i] += 1 # 동명이인을 고려해야 함
        else:
            dict[i] = 1
    for i in completion:
        if i in dict:
            dict[i] -= 1
    for i in dict:
        if dict[i] == 1:
            return i