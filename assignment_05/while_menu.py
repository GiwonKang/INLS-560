### Assignment 05a
# Primes menu option variable
menu_option = ''

# Loop that runs until menu_option is equals to 'q'
while menu_option != 'q':
    # Prints menu options
    print(f'''
    MENU:
    a: cut and shampoo for hairs
    b: receive consultation on hair dying or perming
    q: exit
    ''')

    # Allows user to input a menu options, sets menu_option variable equal to user input
    menu_option = input('Enter your service choice today: ')  # Take input as string
    
    if menu_option == 'a':
        print('We will help you cut and shampoo your hair today.')
    elif menu_option == 'b':
        print('We will give you consultation on hair dying or perming.')
    elif menu_option == 'q':
        print('Thank you for visiting. Goodbye!')
    else:
        print('Invalid option, please choose again.')