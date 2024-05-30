from logics.functions import *
import time

height=10
width=10
board = initializeMap(height, width)

snake = []
placeSnake(board, snake)
direction = ''

for segment in snake:
    board[segment[0]][segment[1]] = 'x'

food = placeFood(board, snake)

while True:
    clearScreen()
    print(board)

    key = input("Enter direction (w/a/s/d): ").strip().lower()
    if key == 'w':
        direction = 'UP'
    elif key == 's':
        direction = 'DOWN'
    elif key == 'a':
        direction = 'LEFT'
    elif key == 'd':
        direction = 'RIGHT'

    head = snake[0][:]
    if direction == 'UP':
        head[0] -= 1
    elif direction == 'DOWN':
        head[0] += 1
    elif direction == 'LEFT':
        head[1] -= 1
    elif direction == 'RIGHT':
        head[1] += 1

    if head in snake or head[0] < 0 or head[0] >= height or head[1] < 0 or head[1] >= width:
        print("Game Over!")
        break

    snake.insert(0, head)
    if head == food:
        food = placeFood(board, snake)
    else:
        tail = snake.pop()
        board[tail[0]][tail[1]] = ' '

    board[head[0]][head[1]] = 'x'
    time.sleep(0.3)

    