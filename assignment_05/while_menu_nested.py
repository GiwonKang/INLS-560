### Assignment 05b
# Primes menu option variable
menu_option = ''

# Loop that runs until menu_option is equals to 'q'
while menu_option != 'q':
    # Prints menu options
    print(f'''
    MENU:
    a: cut and shampoo for hairs
    b: receive consultation on hair dying and perming
    q: exit
    ''')

    # Allows user to input a menu options, sets menu_option variable equal to user input
    menu_option = input('Enter a letter to learn more about our hair salon: ')  # Take input as string
    
    #If menu_option is 'a', prints this statement
    if menu_option == 'a':
        print('We will help you cut and shampoo your hair today.\n')
    # Else, if menu_option is 'b', prints an input statement asking if the user want to receive a consultation on hair dying and perming as well 
    elif menu_option == 'b':
        additional_option = input('Do you want to receive a consultation on hair dying and perming? Enter y or n: ')
        # Response if user's answer is 'y'
        if menu_option == 'y':
            print('Awesome! It would be great to consider dying or perming on vacation!\n')
        # Response if user's answer is 'n'
        else:
            print('Thank you for visiting. Goodbye!\n')