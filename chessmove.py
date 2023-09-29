while True:
    piece_select= input('Select a piece: ')
    move = input('Make a move: ')
    selection = piece_select
    if move in valid_moves and selection != 100:
        white_pieces[selection] = move