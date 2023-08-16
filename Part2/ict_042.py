#이것이 취업을 위한 코딩 테스트다
#예제 4-2
#타입: 구현(완전탐색)
#접근: N은 00~23시. 00시 00분 00초에 대한 3중 for문. -> 최대 24*60*60 -> 86400. Int 배열 기준 4byte *86400 

from sys import stdin as s

s = open("D:/code/python/algo/ict_algo/Part2/input.txt","r")
N = int(s.readline())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                count += 1
print(count)