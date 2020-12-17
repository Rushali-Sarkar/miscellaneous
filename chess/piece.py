#!/bin/usr/python3

SPACE = " "
import checkmove

def castle(move, board_view, piece_view):

    home_rank, king, rook = "1", "K", "R" if move[0] == "O" else "8" , "k" , "r"

    king_before = "e" + home_rank
    rook_before = ("a" if len(move) == 3 else "h") + home_rank

    king_after = ("c" if len(move) == 3 else "g") + home_rank
    rook_after = ("d" if len(move) == 3 else "f") + home_rank

    board_view[king_before] = SPACE
    board_view[king_after] = king

    board_view[rook_before] = SPACE
    board_view[rook_after] = rook

    piece_view[king] = [king_after]
    piece_view[rook].append(rook_after)
    piece_view[rook].remove(rook_before)

    return board_view, piece_view

def not_blocked(board_view, a, b):
    if a > b:
        a, b = b, a

    if a[0] == b[0]:
        between = [a[0] + r for r in "12345678" if a[1] < r < b[1]]
    elif a[1] == b[1]:
        between = [f + a[0] for f in "abcdefgh" if a[0] < f < b[0]]
    else:
        between = DIAGONAL

    return [board_view[sq] for sq in between].count(SPACE) == len(between)


def get_from_square(move, board_view, candidates):
    piece = move[0]
    to_square = move[-2: ]
    if piece in "nN":
        for from_square in candidates:
            if checkmove.check_move(piece, from_square, to_square):
                if not_blocked(board_view, from_square, to_square):
                    return from_square


def move_piece(move, board_view, piece_view):
    piece, to_square = move[0], move[-2: ]
    
    if "x" in move:
        move = move.replace("x", "")
        captured_piece = board_view[to_square]
        piece_view[captured_piece].remove(to_square)

    if len(move) == 5:
        from_square = move[1: 3]
    elif len(piece_view[piece]) == 1:
        from_square = piece_view[piece][0]
    else:
        from_square = get_from_square(move, board_view, piece_view[piece])

    board_view[from_square] = SPACE
    board_view[to_square] = piece

    piece_view[piece].append(to_square)
    piece_view[piece].remove(from_square)
    
    return board_view, piece_view





