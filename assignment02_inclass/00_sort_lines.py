#with open('names.txt','r') as f:
#    lines = f.readlines()

#sorted_lines = sorted(lines, key=lambda line: line[0].lower())

#with open('00_result.txt', 'w') as f:
#    f.writelines(sorted_lines)

def sort_lines(input_file, output_file):
    ''' This is a function that let us put the file names in easier.'''   
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    sorted_lines = sorted(lines, key = lambda line: line[0].lower())

    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

input_file = 'md_list.md'
output_file = '01_results.md'

sort_lines(input_file, output_file)