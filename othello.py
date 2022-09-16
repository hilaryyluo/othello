def check_one_direction(board, turn, row, col, row_inc, col_inc):
  '''
  Returns a True if there is a valid move to be made by checking the inner 8 
    squares around the square location (row, col). Then checks the rest of the 
    row, column, or diagonal (depends on the position of the inner square we are
    checking) to verify that it is a vlaid move. Returns False otherwise.
  
  check_one_direction(): (listof (listof Str)) Str Nat Nat Int Int -> Bool
  Requires: 
    The length of the outer list in board is 8.
    The length of each inner list in board is 8.
    Each string in turn is '', 'B', or 'W' 
  '''
  isinnercircle = True
  if turn == "B":
    oppositecolour = "W"
  else:
    oppositecolour = "B"
  while (row < 7) and (col < 7):
    row = row + row_inc
    col = col + col_inc
    if isinnercircle:
      if board[row][col] != oppositecolour:
        return False
      isinnercircle = False
    else:
      if board[row][col] == turn:
        return True
      elif board[row][col] == "":
        return False
  return False


def othello(board, turn, row, col):
  '''
  Returns True if the piece of colour turn can be played at the given location, 
    (row, col), as a valid move and False otherwise.
  
  othello(): (listof (listof Str)) Str Nat Nat -> Bool
  Requires: 
    The length of the outer list in board is 8.
    The length of each inner list in board is 8.
    Each string in turn is '', 'B', or 'W'   
  
  Examples:
    If board = [[ '',  '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '', 'B', 'B', 'B',  '',  '',  ''],
                  [ '', 'W', 'B', 'W', 'W',  '', 'B',  ''],
                  [ '', 'W', 'B', 'W', 'W', 'W', 'W',  ''],
                  [ '',  '', 'W', 'W', 'W',  '',  '',  ''],
                  [ '',  '',  '', 'W',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  '',  '']]
    othello(board, 'B', 3, 0) => True
    othello(board, 'W', 3, 0) => False
    
    If board2 = [[ 'B', 'W', 'B', 'B', 'B', 'W', 'W', 'W'],
                   [ 'B', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
                   [ 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
                   [ 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'],
                   [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
                   [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
                   [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]
    othello(board2, 'W', 1, 2) => False
  '''
  if board[row][col] != "":
    return False
  directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], \
                [1, 1]]
  for thisdirection in directions:
    if check_one_direction(board, turn, row, col, thisdirection[0], \
                           thisdirection[1]):
      return True
  return False
