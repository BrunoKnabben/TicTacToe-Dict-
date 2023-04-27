from itertools import cycle
import os

board = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' '
}

def resetGame():
    board = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' '
}
    return board

def validaEmpate(board):
    emptyCell = False
    for cell in board.items():
        if cell[1] == ' ':
            emptyCell = True
            
    if emptyCell:
        return False
    else:
        return True

gameOn = True
players = cycle(['Jogador 1', 'Jogador 2'])

def playerMove(jogador, board):
    valid = False

    while not valid:
        requested = input(f'Movimento: ')
        if requested in '1 2 3 4 5 6 7 8 9'.split() and board[f'{str(requested)}'] == ' ':
            if jogador == 'Jogador 1':
                board[f'{str(requested)}'] = 'X'
            else:
                board[f'{str(requested)}'] = 'O'
            valid = True

def hasWinner(board):
    winnerLabel = ''

    #verifica vitórias verticais
    for col in '1 2 3' .split():
        if board[f'{str(int(col) + 3)}'] == board[f'{col}'] and board[f'{str(int(col) + 3)}'] != ' ':
            if board[f'{str(int(col) + 6)}'] == board[f'{col}']:
                winnerLabel = board[f'{col}']

    #verifica vitórias horizontais
    for row in '1 4 7' .split():
        if board[f'{str(int(row) + 1)}'] == board[f'{row}'] and board[f'{str(int(row) + 1)}'] != ' ':
            if board[f'{str(int(row) + 2)}'] == board[f'{row}']:
                winnerLabel = board[f'{row}']

    #verificar vitórias diagonais
    if (board['5'] == board['1'] and board['5'] == board['9'] and board['5'] != ' ') or (board['5'] == board['3'] and board['5'] == board['7'] and board['5'] != ' '):
        winnerLabel = board['5']

    return winnerLabel

def informaJogador(players):
    jogador = next(players)
    return jogador

def imprimeBoard(board):
    print()
    print(' ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'] )
    print('---+---+---')
    print(' ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'] )
    print('---+---+---')
    print(' ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] )
    print()

while gameOn:
    jogador = informaJogador(players)
    os.system('cls')
    print(f'Turno do {jogador}')
    imprimeBoard(board)
    
    playerMove(jogador, board)
    if hasWinner(board) != '':
        os.system('cls')
        imprimeBoard(board)
        print(f'{jogador} venceu!')
        if input('Jogar novamente? [S/N] ').upper() == 'S':
            board = resetGame()
        else:
            break

    if validaEmpate(board):
        gameOn = False
        os.system('cls')
        imprimeBoard(board)
        print('Empatou!')   
