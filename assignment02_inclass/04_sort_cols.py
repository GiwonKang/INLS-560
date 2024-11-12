def sort_file_by_columns(input_file, output_file, primary_index = 2, secondary_index = 1, delimiter = ',', reverse = False):
    # Open the input file and read all lines
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Separate the first two lines (unsorted) and the rest (to be sorted)
    header = lines[:1]
    body = lines[1:]

    # Sort the body by primary and secondary columns (case-insensitive)
    sorted_body = sorted(
        body,
        key = lambda line: (
            line.split(delimiter)[primary_index].lower(), # Primary sort
            line.split(delimiter)[secondary_index].lower() # Secondary sort
        ),
        reverse = reverse   # Apply reverse soritng if needed
    )

    # Combine the header and sorted body
    sorted_lines = header + sorted_body

    # Write the result to the output file
    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

# Specify input and output file names
input_file = 'names_ages.csv'
output_file = 'names_ages_results.csv'

# Sort by the first column, then by the second column
sort_file_by_columns(input_file, output_file, primary_index = 2, secondary_index = 1, delimiter = ',', reverse = False)