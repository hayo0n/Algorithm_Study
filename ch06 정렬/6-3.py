# 두 배열의 원소 교체
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 오름차순 정렬
b.sort(reverse = True) # 내림차순 정렬

# 첫번째 인덱스부터 확인하면서 두 배열의 원소를 최대 k번 비교
for i in range(k):
    if a[i] < b[i]: # a의 원소가 b보다 작은 경우
        a[i], b[i] = b[i], a[i]
    else: # a의 원소가 b의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력