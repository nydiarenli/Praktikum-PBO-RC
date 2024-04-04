import random

board = [['?' for _ in range(3)] for _ in range(3)]

bomb_row, bomb_col = random.randint(0, 2), random.randint(0, 2)

safe_boxes_opened = 0

while True:
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if row == bomb_row and col == bomb_col:
        board[row][col] = 'X'
        print("Yikes, you found a bomb. The end hiks hiks :(")
        break
    else:
        board[row][col] = 'O'
        safe_boxes_opened += 1
        print("Well, there's no bomb here. Congrats babygirl!")

    for r in board:
        print(' '.join(r))

    if safe_boxes_opened == 8:  # 8 safe boxes in a 3x3 grid
        print("You've opened all safe boxes. You win the game!")
        break
