from input1 import input1 as input
#N = int(input())
#for i in range(N):
#    temp = list(map(lambda x: int(x), input().split()))
#    print(temp)

#아이디어
# 가장 큰수를 K번 더한다. 다음은 두번째로 큰 수를 더한다. 총 더하는 횟수 M에 맞게 조절한다.
# M//(K+1)번 -> 큰수 * K + 두번째큰수
# M%(k+1)번  -> 큰수 * (M%(k+1))

#정당성
# 가장 큰 값을 만드는데 최선은 큰수 * K이다.
# 연속되선 안되므로 그 다음 큰수를 더해야한다. 세번째, 네번째로 큰 수를 더하면 두번째 큰 수를 더한 것보다 결과값이 작다.

#전처리
temp_list = list(map(lambda x: int(x), input().split()))
N = temp_list[0]; M = temp_list[1]; K = temp_list[2]
num_list = list(map(lambda x: int(x), input().split()))

#가장 큰 수 2개 뽑기
num_list.sort(reverse= True)
BIGGEST = num_list[0]
SECOND  = num_list[1]

#아이디어 구현 연산
result = (M//(K+1))*(BIGGEST * K + SECOND) + (M%(K+1))*BIGGEST
print(result)