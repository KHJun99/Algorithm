king, queen, rook, bishop, knight, pawn = map(int, input().split())

card = [king, queen, rook, bishop, knight, pawn]

basic = [1, 1, 2, 2, 2, 8]

for i in range(len(card)):
    print(basic[i] - card[i], end = " ")