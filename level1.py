from collections import Counter

def count_puzzle_pieces(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    pieces = lines[1:]
    piece_counts = Counter(pieces)

    output_file_path = file_path.replace('.in', '-output.txt')
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(f"{count} {piece}\n" for piece, count in piece_counts.items())

def main():
    for i in range(1, 6):
        file_name = f"level1_{i}.in"
        count_puzzle_pieces(file_name)

if __name__ == "__main__":
    main()
