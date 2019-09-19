def placePiece(field, c):
    piece = c[0]
    j = ord(c[1]) - 97
    i = 8 - int(c[2])
    field[i][j] = piece
    return piece, i, j
def asterisk(field, i, j):
    if i in range(8) and j in range(8):
        field[i][j] = "*"
        return True
    else:
        return False
def genK(field, i, j):
    count = 0
    count += int(asterisk(field, i+2, j+1))
    count += int(asterisk(field, i+2, j-1))
    count += int(asterisk(field, i-2, j+1))
    count += int(asterisk(field, i-2, j-1))
    count += int(asterisk(field, i+1, j+2))
    count += int(asterisk(field, i+1, j-2))
    count += int(asterisk(field, i-1, j+2))
    count += int(asterisk(field, i-1, j-2))
    return count
def genQ(field, i, j):
    count = 0
    for k in range(1, 8):
        count += int(asterisk(field, i+k, j+k))
        count += int(asterisk(field, i+k, j-k))
        count += int(asterisk(field, i-k, j+k))
        count += int(asterisk(field, i-k, j-k))
        count += int(asterisk(field, i+k, j))
        count += int(asterisk(field, i-k, j))
        count += int(asterisk(field, i, j+k))
        count += int(asterisk(field, i, j-k))
    return count
board = []
for i in range(8):
    board.append(['.'] * 8)
c = input()
piece, i, j = placePiece(board, c)
if piece == "K":
    count = genK(board, i, j)
elif piece == "Q":
    count = genQ(board, i, j)
print(count)
for row in board:
    print(" ".join(row))