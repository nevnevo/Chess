import Square_Info

#True = White, False = Black
color = True
board = []
for c in range(8):
    row = []
    for r in range(8):
        if c%2 + r%2 == 0:
            color = True
        else:
            color = False
        a = Square_Info.Square_Info(color,(c, r), False, False, False)

        row.append(a)

    board.append(row)