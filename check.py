import sys

def print_and_write_lines_range(input_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            write_line = False
            for line_number, line in enumerate(input_file, 1):
                if "write" in line:
                    write_line = True
                    if "DumpDelete" in line:
                        print("Bad block " + line_number)
                else:
                    write_line = False

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except IOError:
        print(f"Error: Unable to read the file '{input_file_path}' or write to '{output_file_path}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path> <output_file_path> <n> <m>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    print_and_write_lines_range(input_file_path)

