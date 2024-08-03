# 큰 수의 법칙
n,m,k=5,8,3
data=[2,4,5,4,6]

data.sort()
first=data[-1]
second=data[-2]

count=(m//(k+1))*k+m%(k+1)

result=0
result+=count*first
result+=(m-count)*second

print(result)