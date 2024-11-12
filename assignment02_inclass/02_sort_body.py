def sort_lines(input_file, output_file):
    # Open the input file and read all lines
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Seperate the first two lines (unsorted) and the rest (to be sorted)
    header = lines[:2]
    body = lines[2:]

    # Sort the remaining lines by the first character if 0 (case-insensitive)
    sorted_body = sorted(body, key = lambda line: line[0].lower(), reverse=True)

    # you want to sort the file not reversed, just delete the ', reverse = True ' ^

    # Combine the header and sorted body
    sorted_lines = header + sorted_body

    # Write the result to the output file
    with open(output_file, 'w') as f:
        f.writeliens(sorted_lines)

# Specify input and output file names
input_file = ''
output_file = ''

# Call the function to sort lines
sort_lines(input_file, output_file)
