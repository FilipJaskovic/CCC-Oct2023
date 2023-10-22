import os
from collections import Counter

def normalize_piece(piece):

    piece_chars = piece.split(',')
    rotations = [piece_chars[i:] + piece_chars[:i] for i in range(4)]

    rotation_strs = [','.join(rotation) for rotation in rotations]
    rotation_strs.sort()
    
    return rotation_strs[0]

def count_puzzle_pieces(file_path, output_file_path):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_pieces = int(lines[0].strip())
    pieces = [line.strip() for line in lines[1:]]

    normalized_pieces = [normalize_piece(piece) for piece in pieces]
    piece_counts = Counter(normalized_pieces)

    output_lines = [f"{count} {piece}" for piece, count in piece_counts.items()]

    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(output_lines))

    print(f"Output written to {output_file_path}")

input_file_path = 'level2_5.in'
output_file_path = 'level2_5-output.txt' 
count_puzzle_pieces(input_file_path, output_file_path)
