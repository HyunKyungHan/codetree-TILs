def move(dir, dist):
    if dir == 'E':
        nx, ny = cur_x + dist*dx[0], cur_y + dist*dy[0]
    if dir == 'S':
        nx, ny = cur_x + dist*dx[1], cur_y + dist*dy[1]
    if dir == 'W':
        nx, ny = cur_x + dist*dx[2], cur_y + dist*dy[2]
    if dir == 'N':
        nx, ny = cur_x + dist*dx[3], cur_y + dist*dy[3]

    return nx, ny

if __name__ == '__main__':
    N = int(input())
    commands = []
    for i in range(N):
        commands.append(list(input().split()))
    
    cur_x, cur_y = 0,0
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 동 남 서 북
    
    for i in range(N):
        dir = commands[i][0]
        distance = int(commands[i][1])
        cur_x, cur_y = move(dir, distance)
        move(dir, distance)
    
    print(cur_x, cur_y)