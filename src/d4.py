file1 = open('d4.txt', 'r')
task_input = [line.strip() for line in file1.readlines()]


class BingoField:
    def __init__(self, value: int):
        self.value = value
        self.checked = False


class BingoBoard:

    def __init__(self):
        self.rows = []
        self.completed = False

    def add_row(self, raw_string: str):
        row = []
        for v in [s.strip() for s in raw_string.split()]:
            row.append(BingoField(int(v)))
        self.rows.append(row)

    def update_field_with_value(self, value: int):
        for row in self.rows:
            for col_idx in range(len(row)):
                field = row[col_idx]
                if field.value == value:
                    field.checked = True
                    self.completed = self._is_completed(row, col_idx)

    def not_checked_sum(self):
        unchecked_sum = 0
        for row in self.rows:
            for field in row:
                if not field.checked:
                    unchecked_sum += field.value
        return unchecked_sum

    def _is_completed(self, row, col_idx):
        return self._is_col_completed(col_idx) or self._is_row_completed(row)

    def _is_col_completed(self, col_idx):
        for row in self.rows:
            if not row[col_idx].checked:
                return False
        return True

    def _is_row_completed(self, row):
        for field in row:
            if not field.checked:
                return False
        return True


def init_bingo_boards(input_data):
    boards = []
    current_board = BingoBoard()
    for line in input_data[2:]:
        if line == "":
            boards.append(current_board)
            current_board = BingoBoard()
        else:
            current_board.add_row(line)

    boards.append(current_board)
    return boards


def play_bingo(input_data):
    boards = init_bingo_boards(input_data)
    numbers_to_draw = task_input[0].split(",")
    for drawn_number in numbers_to_draw:
        for board in boards:
            board.update_field_with_value(int(drawn_number))
            if board.completed:
                boards = [b for b in boards if not b.completed]
                if not boards:
                    return board.not_checked_sum() * int(drawn_number)


print(play_bingo(task_input))
