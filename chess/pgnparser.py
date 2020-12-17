#!/usr/bin/python3
import re
FILES = "abcdefgh"
RANKS = "12345678"
SPACE = " "

def pgn_to_moves(game_file: str) -> [str]:
    raw_pgn = SPACE.join([line.strip() for line in open(game_file)])

    # * * * * * * * * * * * * * * * * * * * * * * * * * 
    # pre-process comments to enable regex
    # Remove comments      = text within {}
    # * * * * * * * * * * * * * * * * * * * * * * * * *
    comments_marked = raw_pgn.replace("{", "<").replace("}", ">")
    STRC = re.compile("<[^>]*>")
    comments_removed = STRC.sub(" ", comments_marked)

    # * * * * * * * * * * * * * * * * * * * * * * * * *
    # pre-process STR to enable regex
    # Remove STR      = text within[]
    # * * * * * * * * * * * * * * * * * * * * * * * * *
    STR_marked = comments_removed.replace("[", "<").replace("]", ">")
    str_removed = STRC.sub(SPACE, STR_marked)

    # * * * * * * * * * * * * * * * * * *     * * * * * * * 
    # Remove move numbers
    # * * * * * * * * * * * * * * * * * *     * * * * * * * 
    MOVE_NUM = re.compile("[1-9][0-9]* *\.")
    just_moves = [_.strip() for _ in MOVE_NUM.split(str_removed)]

    # * * * * * * * * * * * * * * * * * *     * * * * * * * 
    # Remove final result
    # * * * * * * * * * * * * * * * * * *     * * * * * * * 
    last_move = just_moves[-1]
    RESULT = re.compile("( *1 *- *0 *- *- *- *1 *| *1/2 *- *1/2 *)")
    last_move = RESULT.sub("", last_move)

    return [pre_process_a_move(_) for _ in just_moves[1: -1]] + [pre_process_last_move(last_move)]

def clean(raw_move: str) -> str:
    # * * * * * * * * * * * * * * * * * *     * * * * * * * 
    # Remove CHECK +, MATE # dots in e.p = and
    #        ANNOTATIONS !?
    # * * * * * * * * * * * * * * * * * *     * * * * * * * 
    return ''.join(filter(str.isalnum, raw_move))

def pre_process_a_move(move: str) -> (str, str):
    wmove, bmove = move.strip().split()
    if wmove[0] in FILES and wmove[1] in RANKS + "x":
        wmove = "P" + wmove
    if bmove[0] in FILES and bmove[1] in RANKS + "x":
        bmove = "P" + bmove
    else:
        bmove = bmove.lower()

    return clean(wmove), clean(bmove)

