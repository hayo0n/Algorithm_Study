# 위에서 아래로
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리 사용
array  = sorted(array,reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
    print(i, end=' ')