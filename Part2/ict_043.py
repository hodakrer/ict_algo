#이것이 취업을 위한 코딩 테스트다
#예제 4-3
#타입: 구현(완전탐색)
#접근: 이론상 나이트가 도착할 수 있는 곳은 8곳이다. 입력값에서 움직일 수 있는 8곳이 테이블 위인지만 판단하면 된다.
#      체스판의 크기는 8*8이다.
#cur_x, cur_y: 체스말 현재 위치
#chess_y: 입력값 x좌표가 알파벳인 걸 Int값으로 바꿔주기 위한 리스트
#dx, dy: 입력값 좌표에서 움직일 수 있는 이동방향값
from sys import stdin as s

s = open("D:/code/python/algo/ict_algo/Part2/input.txt","r")
N = str(s.readline())
cur_x = int(N[1])
cur_y = N[0]
chess_y = ['_','a','b','c','d','e','f','g','h']
cur_y = int(chess_y.index(cur_y))
count = 0
#     왼쪽,  오른쪽,   윗쪽,  오른쪽
dx = [-1,  1, -1, 1, -2, -2,  2, 2]
dy = [-2, -2,  2, 2, -1,  1, -1, 1]
#8방향 체크
for i in range(8):
    if cur_x + dx[i] <= 8 and cur_x + dx[i] >= 1 and cur_y + dy[i] <= 8 and cur_y + dy[i] >= 1:
        count += 1
print(count)