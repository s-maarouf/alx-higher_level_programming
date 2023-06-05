#!/usr/bin/python3

"""Define Nqueens puzzle"""
import sys


class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def solve(self):
        self.backtrack([], 0)
        self.print_solutions()

    def backtrack(self, positions, row):
        if row == self.n:
            self.solutions.append(positions[:])
            return

        for col in range(self.n):
            if self.is_valid(positions, row, col):
                positions.append([row, col])
                self.backtrack(positions, row + 1)
                positions.pop()

    def is_valid(self, positions, row, col):
        for pos in positions:
            if pos[1] == col or \
               pos[1] - pos[0] == col - row or \
               pos[1] + pos[0] == col + row:
                return False
        return True

    def print_solutions(self):
        for solution in self.solutions:
            print(solution)
        print()


def main():

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(n)
    solver.solve()


if __name__ == "__main__":
    main()
