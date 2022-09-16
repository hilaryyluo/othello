from othello import othello

def test1():
    board = [[ '',  '',  '',  '',  '',  '',  '',  ''],
            [ '',  '',  '',  '',  '',  '',  '',  ''],
            [ '',  '', 'B', 'B', 'B',  '',  '',  ''],
            [ '', 'W', 'B', 'W', 'W',  '', 'B',  ''],
            [ '', 'W', 'B', 'W', 'W', 'W', 'W',  ''],
            [ '',  '', 'W', 'W', 'W',  '',  '',  ''],
            [ '',  '',  '', 'W',  '',  '',  '',  ''],
            [ '',  '',  '',  '',  '',  '',  '',  '']]
    assert othello(board, 'B', 3, 0) == True
    assert othello(board, 'W', 3, 0) == False

def test2():
    board2 = [[ 'B', 'W', 'B', 'B', 'B', 'W', 'W', 'W'],
            [ 'W', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            [ 'B', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
            [ 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [ 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'],
            [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
            [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
            [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]
    assert othello(board2, 'W', 1, 2) == False 

def test3():
    board = [[ '',  '',  '',  '',  '',  '',  '',  ''],
            [ '',  '',  '',  '',  '',  '',  '',  ''],
            [ '',  '', 'B', 'B', 'B',  '',  '',  ''],
            [ '', 'W', 'B', 'W', 'W',  '', 'B',  ''],
            [ '', 'W', 'B', 'W', 'W', 'W', 'W',  ''],
            [ '',  '', 'W', 'W', 'W',  '',  '',  ''],
            [ '',  '',  '', 'W',  '',  '',  '',  ''],
            [ '',  '',  '',  '',  '',  '',  '',  '']]
    assert othello(board, 'B', 3, 3) == False
    assert othello(board, 'W', 1, 3) == True
    assert othello(board, 'B', 5, 5) == True
    assert othello(board, 'W', 7, 7) == False
         
def test4():
    board2 = [[ 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            [ 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B'],
            [ 'B', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
            [ 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [ 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'],
            [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
            [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
            [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]
    assert othello(board2, 'B', 2, 3) == False
    assert othello(board2, 'W', 7, 1) == False