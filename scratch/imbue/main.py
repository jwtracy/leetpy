from collections import deque
import pprint

boards = [
    '''...............
...............
...............
...............
...............
...............
.ZYMURGY.......
.......E.......
.......L.......
.......L.......
.......O.......
.......WIND....
.........A.....
.........N.....
...............''',
    '''...............
...............
...............
...............
...............
...............
ZYMURGY..G.....
......E..R.....
......L..O.....
......L..U.....
......O..N.....
......WIND.....
...............
...............
..............''',
    '''...............
...............
...............
...............
...............
...............
.ZYMURGY..GOOD.
.......E..R.DO.
.......L..O....
.......L..U....
.......O..N....
.......WIND....
...............
...............
...............''',
    '''...............
...............
...............
...............
...............
...............
.ZYMURGY..GOOD.
.......E..R....
.......L..O....
.......L..U....
.......O..N....
.......WIND...N
..............O
..............N
...........NONE'''
]

def is_scrable_word(s: str) -> bool:
    words = set()
    with open("./dictionary.txt", "r") as dict_file:
        for word in dict_file:
            words.add(word.strip("\n\r "))
    return s in words

def other_chars(s: str, i: int) -> str:
    if i+1 >= len(s):
        return s[0:i]
    return s[0:i] + s[i+1:]

def all_valid_words(s: str) -> list[str]:
    res = set()
    q = deque([
        (c, other_chars(s, i)) for i, c in enumerate(s)
    ])
    while q:
        node = q.popleft()
        word = node[0]
        if is_scrable_word(word):
            res.add(word)

        for i, c in enumerate(node[1]):
            q.append((node[0]+c, other_chars(node[1], i)))

    return list(res)

def is_valid_board(board_str: str) -> bool:
    board = []
    lines = board_str.splitlines()
    for l in lines:
        board.append([c for c in l])
    # pprint.pp(board)

    if board[len(board)//2][len(board[0])//2] == ".":
        print("not centered")
        return False

    for i in range(len(board)):
        current = ""
        for j in range(len(board[0])):
            if board[i][j] != ".":
                current += board[i][j]
            elif current != "":
                if len(current) > 1 and not is_scrable_word(current):
                    print(f"{current} is not a valid scrabble word in row {i}")
                    return False
                current = ""

    for j in range(len(board[0])):
        current = ""
        for i in range(len(board)):
            if board[i][j] != ".":
                current += board[i][j]
            elif current != "":
                if len(current) > 1 and not is_scrable_word(current):
                    print(f"{current} is not a valid scrabble word in col {j}")
                    return False
                current = ""

    seen = set()
    def dfs(i: int, j: int):
        if (i, j) in seen:
            return
        seen.add((i,j))
        if i+1 < len(board) and board[i+1][j] != ".": dfs(i+1,j)
        if i-1 >= 0 and board[i-1][j] != ".": dfs(i-1,j)
        if j+1 < len(board[0]) and board[i][j+1] != ".": dfs(i,j+1)
        if j-1 >= 0 and board[i][j-1] != ".": dfs(i,j-1)

    graph_count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "." and (i,j) not in seen:
                graph_count += 1
                if graph_count > 1:
                    print("board is not connected")
                    return False
                dfs(i,j)
    return True

def main() -> None:
    assert is_scrable_word("DDA") == False
    assert is_scrable_word("ADD") == True

    print(all_valid_words("DDA"))
    print(all_valid_words("SBAD"))

    print([is_valid_board(b) for b in boards])


if __name__ == "__main__":
    main()