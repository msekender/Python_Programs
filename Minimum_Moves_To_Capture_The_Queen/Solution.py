'''
Solution Approach
Modeling the Problem as a Graph Search:

The Rook can move horizontally and vertically.
The Bishop can move diagonally.
We need to find the shortest sequence of valid moves that capture the queen.
Breadth-First Search (BFS):

Treat the board as a graph, where each piece moves to valid positions as nodes.
Use BFS to explore the minimum number of moves required to reach (e, f), the queen’s position.
Handling Obstructions:

Since Rook and Bishop cannot jump over other pieces, we must ensure moves are valid.
'''

from collections import deque

def minMovesToCaptureQueen(a, b, c, d, e, f):
    # Directions for rook (horizontal and vertical moves)
    rook_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Directions for bishop (diagonal moves)
    bishop_moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    # Board representation (8x8)
    board_size = 8
    
    # BFS queue: (x, y, piece_type, moves_count)
    queue = deque([(a, b, "rook", 0), (c, d, "bishop", 0)])
    
    # Visited positions to avoid redundant calculations
    visited = set()
    
    while queue:
        x, y, piece, moves = queue.popleft()
        
        # If reached queen's position, return move count
        if (x, y) == (e, f):
            return moves
        
        # Avoid revisiting the same position with the same piece
        if (x, y, piece) in visited:
            continue
        visited.add((x, y, piece))
        
        # Get valid moves based on the piece type
        moves_list = rook_moves if piece == "rook" else bishop_moves
        
        # Try all possible moves
        for dx, dy in moves_list:
            new_x, new_y = x, y
            # Move until hitting the board boundary
            while 1 <= new_x + dx <= board_size and 1 <= new_y + dy <= board_size:
                new_x += dx
                new_y += dy
                if (new_x, new_y) == (c, d) or (new_x, new_y) == (a, b):  # Cannot jump over pieces
                    break
                queue.append((new_x, new_y, piece, moves + 1))
    
    return -1  # Should never reach here based on problem constraints

# Example Test Cases
print(minMovesToCaptureQueen(1, 1, 8, 8, 2, 3))  # Output: 2
print(minMovesToCaptureQueen(5, 3, 3, 4, 5, 2))  # Output: 1

''' 
Time Complexity Analysis
The rook moves in at most 4 directions.
The bishop moves in at most 4 diagonal directions.
Each move traverses at most O(8), so the worst-case BFS traversal is O(8 × 4) = O(32) ~ O(1) (constant time).
Since 8x8 board is fixed size, BFS operates in constant time O(1).

Space Complexity Analysis
We maintain a queue and a visited set, both storing at most O(64) = O(1) positions.
The space complexity is O(1) since the board size is constant.'
'''

