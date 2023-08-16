#이것이 취업을 위한 코딩 테스트다
#예제 4-1
#타입: 단순구현
from sys import stdin as s

s = open("D:/code/python/algo/ict_algo/Part2/input.txt","r")
N = int(s.readline())
print(N)
command_list = list(map(lambda x:x,s.readline().split()))
print(command_list)
cur_x = 1
cur_y = 1
#U D L R
dx_list = [-1, 1, 0, 0]
dy_list = [ 0, 0,-1, 1]
#command_list대로 움직이기
for i in range(N):
    if   command_list[i] == "U":
        cur_x = max(1, cur_x + dx_list[0])
        cur_y = max(1, cur_y + dy_list[0])
    elif command_list[i] == "D":
        cur_x = min(N, cur_x + dx_list[1])
        cur_y = min(N, cur_y + dy_list[1])
    elif command_list[i] == "L":
        cur_x = max(1, cur_x + dx_list[2])
        cur_y = max(1, cur_y + dy_list[2])
    elif command_list[i] == "R":
        cur_x = min(N, cur_x + dx_list[3])
        cur_y = min(N, cur_y + dy_list[3])
print(cur_x, ' ',cur_y)