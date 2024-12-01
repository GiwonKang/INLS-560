import sys # don't use quit() or exit() in production code. use sys.exit

# Make program repeat:
while True:

    # get user input for file:
    file_variable = input('''what file would you like to search for?:
    a) 60s-music file
    b) athletes file
    x) to exit
    ''')


    # process user input
    if file_variable == 'x':
        sys.exit() # this requires
    elif file_variable == 'a':
        file_variable = '60s-music.csv'
    elif file_variable == 'b':
        file_variable = 'athletes.csv'
    else:
        print('Invalid option. Please select a,v, or x.')
        continue
    
    # enter a search term this // is a global variable
    search_variable = input(f'Enter the search term for {file_variable} file: ')
    search_variable = search_variable.title() # Make it so that the user can enter lower-case term.


    # go to 02_search_for term. to continue .....
    def find(file_variable, search_variable):
        with open(file_variable, 'r') as file:
            content = file.read()
    # now check to the file is in the memory buffer as content

    # Next check to see if the search_variable is in the content buffer:
            if search_variable in content:

            # if the file print that it is in the file AND
            # if user wants to see the entries for the term
                print(f'Your search term {search_variable} exist in the {file_variable} file:')
                see_entries = input('Would you like to see the entries? (y or n)?')

                # if y then run this code to output all the entreis:
                if see_entries.lower() == 'y':
                    print(f'Here are all of the entries with the term {search_variable}:')
                    with open(file_variable, 'r') as file:
                        for line in file:
                            if search_variable in line: #
                                print(line.strip())
                
                
                
                # if N lowercase (user does not want to ) then run this code:
                elif see_entries.lower() == 'n':
                    print('Goodbye')
                    sys.exit()

                else:
                    print(f"Invalid option. Please entry y or n.")
                
            
            # if it is not, print that it is there
            else:
                print(f'{search_variable} does not exist in {file_variable}')

    # call the function
    find(file_variable, search_variable)