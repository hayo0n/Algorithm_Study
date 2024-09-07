def solution(array, commands):
    answer = []
    for com in commands:
        i, j, k = com
        answer.append(list(sorted(array[i-1:j])[k-1]))
    return answer

2
3
4
5
6
7
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer