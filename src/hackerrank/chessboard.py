

if __name__ == "__main__":
    xl1, xr1, yl1, yr1, xl2, xr2, yl2, yr2 = (int(input()) for _ in range(8))
    board = [[-1]*9 for _ in range(9)]
    black1, white1 = 0, 0
    black2, white2 = 0, 0
    for i in range(xl1, xr1 + 1):
        for j in range(yl1, yr1 + 1):
            color = i % 2 ^ j % 2
            board[i][j] = color
            if color == 0: # odd, odd and even, even : 0(B), else 1(W)
                black1 += 1
            else:
                white1 += 1
    for i in range(xl2, xr2 + 1):
        for j in range(yl2, yr2 + 1):
            color = i % 2 ^ j % 2
            if board[i][j] == -1:
                if color == 0:
                    black2 += 1
                else:
                    white2 += 1 
    count = 0
    if black1 > 0 and black2 > 0:
        count = black1 + black2
    if white1 > 0 and white2 > 0:
        count += white1 + white2
    
    print(count)