import sys

def print_and_write_lines_range(input_file_path, output_file_path, n, m):
    try:
        with open(input_file_path, 'r') as input_file:
            with open(output_file_path, 'w') as output_file:
                for line_number, line in enumerate(input_file, 1):
                    if n <= line_number <= m:
                        output_file.write(line)
                    if line_number == m:
                        break
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except IOError:
        print(f"Error: Unable to read the file '{input_file_path}' or write to '{output_file_path}'.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <input_file_path> <output_file_path> <n> <m>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    n = int(sys.argv[3])
    m = int(sys.argv[4])
    print_and_write_lines_range(input_file_path, output_file_path, n, m)

