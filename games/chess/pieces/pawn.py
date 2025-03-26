
from typing import Literal


class Pawn:
    def __init__(self, x, y, color) -> None:
        self.x: int = x
        self.y: int = y

        if color not in ('white', 'black'):
            raise ValueError("Color must be 'white' or 'black'.")
        self.color: str = color

        self.general_direction: Literal[1] | Literal[-1] = 1 if color == 'white' else -1
        self.allowed_forwards = 1
        

    def move_forward(self) -> None:
        self.y = self.general_direction * (self.y + self.allowed_forwards) 
    

    def move_diagonally_forward(self, x_direction: Literal[1] | Literal[-1]) -> None:
        if not (x_direction == 1 or x_direction == -1):
            raise ValueError("The specified direction must be either 1 or -1.")
        self.x += x_direction
        self.move_forward()


def main() -> None:
    pass

if __name__ == '__main__':
    main()