import sys
import random

def main():
    if len(sys.argv) != 5:
        print("Usage: python3 make_vacuum_world.py <rows> <cols> <blocked_fraction> <num_dirty>")
        sys.exit(1)

    # Parse arguments
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    blocked_fraction = float(sys.argv[3])
    num_dirty = int(sys.argv[4])

    # Initialize grid
    grid = [['_' for _ in range(cols)] for _ in range(rows)]

    # Place blocked cells
    for r in range(rows):
        for c in range(cols):
            if random.random() < blocked_fraction:
                grid[r][c] = '#'

    # Collect valid positions (non-blocked)
    valid_positions = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '_']

    # Place dirty cells
    random.shuffle(valid_positions)
    dirty_count = min(num_dirty, len(valid_positions))
    for i in range(dirty_count):
        r, c = valid_positions[i]
        grid[r][c] = '*'

    # Update valid positions (exclude dirt)
    valid_positions = [(r, c) for r, c in valid_positions[dirty_count:] if grid[r][c] == '_']

    # Place robot
    if valid_positions:
        r_start, c_start = random.choice(valid_positions)
        grid[r_start][c_start] = '@'

    # Output
    print(cols)
    print(rows)
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    main()