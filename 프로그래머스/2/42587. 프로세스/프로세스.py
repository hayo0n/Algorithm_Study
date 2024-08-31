from collections import deque

def solution(priorities, location):
    answer = 0
    q1 = deque()

    for i, ele in enumerate(priorities):
        q1.append([ele, i])

    priorities.sort(reverse= True)
    q2 = deque(priorities)

    while q1:
        ele = q1.popleft()

        if ele[0] == q2[0]:
            q2.popleft()
            answer += 1

            if ele[1] == location:
                return answer

        else:
            q1.append(ele)

    return -1