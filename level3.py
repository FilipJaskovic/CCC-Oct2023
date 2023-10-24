def read_puzzle(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    size = int(lines[0])
    puzzle = [line.split() for line in lines[1:size + 1]]

    return size, puzzle

def identify_and_correct_mistakes(size, puzzle):
    """
    Identifies and corrects mistakes in a given puzzle.

    Args:
    - size (int): The size of the puzzle.
    - puzzle (list): A 2D list representing the puzzle.

    Returns:
    - A 2D list representing the corrected puzzle.
    """

    directions = [(0, 1), (1, 0)]

    for i in range(size):
        for j in range(size):
            piece = puzzle[i][j].split(',')

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if ni >= size or nj >= size:
                    continue

                neighbor = puzzle[ni][nj].split(',')
                side, neighbor_side = (2, 0) if dx == 1 else (1, 3)

                if piece[side] == neighbor[neighbor_side] and piece[side] in ('K', 'H'):
                    new_piece = neighbor[:]
                    new_piece[neighbor_side] = 'H' if piece[side] == 'K' else 'K'
                    puzzle[ni][nj] = ','.join(new_piece)

    return puzzle

def main():
    for i in range(1, 6):
        file_path = f'level3_{i}.in'
        puzzle_size, puzzle_matrix = read_puzzle(file_path)
        corrected_puzzle = identify_and_correct_mistakes(puzzle_size, puzzle_matrix)

        output_file_path = file_path.replace('.in', '-output.txt')
        with open(output_file_path, 'w') as output_file:
            for row in corrected_puzzle:
                output_file.write(' '.join(row) + '\n')

if __name__ == "__main__":
    main()
