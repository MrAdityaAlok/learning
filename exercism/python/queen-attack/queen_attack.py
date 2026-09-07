from typing import Self


class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")

        if row > 7:
            raise ValueError("row not on board")

        if column < 0:
            raise ValueError("column not positive")

        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.cloumn = column

    def can_attack(self, another_queen: Self) -> bool:
        return self._is_in_line_with(another_queen) or self._is_diagonal_to(
            another_queen
        )

    def _is_in_line_with(self, another_queen: Self) -> bool:
        same_row = self.row == another_queen.row
        same_cloumn = self.cloumn == another_queen.cloumn

        if same_row and same_cloumn:
            raise ValueError("Invalid queen position: both queens in the same square")

        return same_row or same_cloumn

    def _is_diagonal_to(self, another_queen: Self) -> bool:
        return abs(self.row - another_queen.row) == abs(
            self.cloumn - another_queen.cloumn
        )
