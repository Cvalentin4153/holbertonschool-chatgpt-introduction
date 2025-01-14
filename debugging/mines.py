#!/usr/bin/python3
import random
import os

def clear_screen():
    """Clears the console screen on Windows or Unix-like systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height

        # Randomly pick 'mines' unique positions out of width*height
        self.mines = set(random.sample(range(width * height), mines))

        # Track whether each cell is revealed
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """Displays the board to the screen.

        If 'reveal' is True, all mines are shown; otherwise, only revealed cells are shown.
        """
        clear_screen()
        # Print column headers (x-coordinates)
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        # Print each row
        for y in range(self.height):
            # Print row label (y-coordinate)
            print(f'{y:2}', end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    # If it's a mine, show '*'
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        # Otherwise, count adjacent mines
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    # Not revealed yet
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """Counts how many mines are in the adjacent 8 cells."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal_cell(self, x, y):
        """Reveals the cell at (x, y). 
           Returns False if the cell is a mine, otherwise True.
        """
        # If it's a mine, game over
        if (y * self.width + x) in self.mines:
            return False

        # Mark as revealed
        self.revealed[y][x] = True

        # If there are no adjacent mines, automatically reveal neighbors
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    # Check bounds and reveal neighbors that haven't been revealed yet
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal_cell(nx, ny)

        return True

    def play(self):
        """Main game loop for Minesweeper."""
        while True:
            self.print_board()
            try:
                # Read user input for x and y
                x = int(input("Enter x coordinate (0-based): "))
                y = int(input("Enter y coordinate (0-based): "))

                # Check if coordinates are in range
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of range. Please try again.")
                    continue

                # Attempt to reveal the cell
                if not self.reveal_cell(x, y):
                    # If reveal_cell() returns False, it's a mine -> game over
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # (Optional) You could add a victory check here by seeing if all
                # non-mine cells are revealed.

            except ValueError:
                print("Invalid input. Please enter integer coordinates.")

if __name__ == "__main__":
    game = Minesweeper(width=10, height=10, mines=10)
    game.play()

