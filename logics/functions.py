import os
import numpy as np
import random

def clearScreen():
    os.system('cls')

def initializeMap(height, width):
    board = np.full((height, width), ' ')
    return board

def placeFood(board, snake):
    while True:
        foodX = random.randint(0, len(board[0]) - 1)
        foodY = random.randint(0, len(board) - 1)
        if [foodY, foodX] not in snake:
            board[foodY][foodX] = 'o'
            break
    return [foodY, foodX]

def placeSnake(board, snake):
    while True:
        snakeX = random.randint(0, len(board[0]) - 1)
        snakeY = random.randint(0, len(board) - 1)
        if [snakeY, snakeX] not in snake:
            snake.append([snakeY, snakeX])
            break