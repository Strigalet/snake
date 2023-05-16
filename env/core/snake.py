import numpy as np

from settings.constants import DIRECTIONS, SNAKE_BLOCK


class Snake:
    def __init__(self, head_position, direction_index, length):
        """
        @param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        # Information snake need to know to make the move
        self.snake_block = SNAKE_BLOCK
        self.current_direction_index = direction_index
        # Alive identifier
        self.alive = True
        # Place the snake
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for i in range(1, length):
            # Direction inverse of moving

            current_position = current_position - DIRECTIONS[self.current_direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action):
        """
        @param action: int 
        @param return: tuple, tuple
        """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        # Example: if snake looks left, pressing "left" or "right" buttons should change nothing
        if (abs(self.current_direction_index - action) != 2) and (self.current_direction_index != action):
            self.current_direction_index = action
        # Remove tail (can be implemented in 1 line)
        head_x, head_y = self.blocks[0][0], self.blocks[0][1]
        tail = self.blocks.pop()
        # Create new head
        if self.current_direction_index == 3:
            new_head_x, new_head_y = head_x, head_y - 1
        if self.current_direction_index == 1:
            new_head_x, new_head_y = head_x, head_y + 1
        if self.current_direction_index == 0:
            new_head_x, new_head_y = head_x - 1, head_y
        if self.current_direction_index == 2:
            new_head_x, new_head_y = head_x + 1, head_y
        new_head = (new_head_x, new_head_y)
        # Add new head
        # Note: all Snake's coordinates should be tuples (X, Y)
        self.blocks = [new_head] + self.blocks
        return new_head, tail