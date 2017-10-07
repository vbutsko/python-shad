import queue


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def wave(x, y, w, h, matrix):
    queue_point = queue.Queue()
    queue_point.put((x, y, 1))
    while not queue_point.empty():
        x, y, deep = queue_point.get()
        for i in range(0,4):
            if (0 <= x + dx[i] < w) and (0 <= y + dy[i] < h):
                if matrix[x + dx[i]][y + dy[i]] == 0:
                    matrix[x + dx[i]][y + dy[i]] = deep + 1
                    queue_point.put((x + dx[i], y + dy[i], deep + 1))
    return matrix


def solve():
    matrix = []
    rdl = list(map(int, input().split()))
    x_0, y_0 = 0, 0
    w, h = rdl
    for j in range(w):
        rdl = input()
        cur = []
        for k in range(h):
            if rdl[k] == '.':
                cur.append(0)
            elif rdl[k] == '#':
                cur.append(-1)
            else:
                x_0, y_0 = j, k
                cur.append(1)
        matrix.append(cur)
    return wave(x_0, y_0, w, h, matrix)


result = solve()
for j in result:
    print (' '.join(str(x if x == -1 else x - 1) for x in j))