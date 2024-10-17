import random


class Node:
    def __init__(self, board, father_score=None):
        self.score = None
        self.nodes = []

        self.score = win(board)
        if self.score or not board.count(0):
            return

        piece = 1 if board.count(0) % 2 else -1
        self.score = -2 if piece == 1 else 2
        father_score = father_score if father_score is not None else -1 * self.score

        for i in range(9):
            if board[i]:
                self.nodes.append(None)
            else:
                temp = board.copy()
                temp[i] = piece
                self.nodes.append(Node(temp, self.score))
                if piece == 1 and self.nodes[-1].score > self.score or piece == -1 and self.nodes[-1].score < self.score:
                    self.score = self.nodes[-1].score
                    # self.score == father_score，可剪更多枝，此时不会有更好的结果，但可能有更差的结果，取决于需要获取当前局面的什么信息
                    if piece == 1 and self.score > father_score or piece == -1 and self.score < father_score:
                        return


def win(board):
    for piece in [1, -1]:
        for i in range(3):
            if piece == board[3 * i] == board[3 * i + 1] == board[3 * i + 2] or piece == board[i] == board[i + 3] == board[i + 6]:
                return piece
        if piece == board[0] == board[4] == board[8] or piece == board[2] == board[4] == board[6]:
            return piece
    # 未结束或和棋
    return 0


def operate(board):
    node = Node(board)

    index = random.sample([i for i in range(9) if node.nodes[i] and node.nodes[i].score == node.score], 1)[0]
    piece = 1 if board.count(0) % 2 else -1

    return index, piece


def start():
    board = [0 for _ in range(9)]
    first = input("X or O?").strip().lower() == "x"
    people_piece = 1 if first else -1

    while True:
        print("\n".join("".join("X" if board[i + 3 * j] == 1 else "O" if board[i + 3 * j] == -1 else str(i + 3 * j) for i in range(3)) for j in range(3)), end="\n" + "-" * 20 + "\n")

        winner = win(board)
        if winner or not board.count(0):
            print("X win" if winner == 1 else "O win" if winner == -1 else "draw")
            break

        if first:
            index = input("%s = " % ("X" if people_piece == 1 else "O"))
            if not index.isdigit() or not 0 <= int(index) <= 8 or board[int(index)]:
                print("illegal")
                continue
            board[int(index)] = people_piece
        else:
            index, computer_piece = operate(board)
            board[index] = computer_piece
            print("%s = %d" % ("X" if people_piece == -1 else "O", index))

        first = not first


start()
