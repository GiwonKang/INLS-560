### Assignment 04
# Constants for high and low temperature
MIN_YEARS_DRIVING = 3
MIN_YEARS_USE_INSURANCE = 2

years_driving = int(input('Enter your years of driving: '))
years_insurance = int(input('Enter how many years you have been used our car insurance : '))

if years_driving >= MIN_YEARS_DRIVING and years_insurance >= MIN_YEARS_USE_INSURANCE:
    print('Congratulations! You are eligible for purchasing our premium car insurance.')
else:
# Multi-line with f-string
    print(f'''
    Sorry, you do not meet the requirements for purchasing our premium car insurance.

    You need at least:
    - {MIN_YEARS_DRIVING} years of driving
    - {MIN_YEARS_USE_INSURANCE} years for using our car insurance
    ''')

# TARGET A
# TARGET B
# CONDITION

# Constants for Sales Manager Position
# MIN_YEARS_SALES = 2
# MIN_YEARS_TOP_AWARD = 1

# years_sales = int(input('Enter your years of sales experience: '))
# years_top_award = int(input('Enter how many years you have been sales person of the year: '))

# if years_sales >= MIN_YEARS_SALES and years_top_award >= MIN_YEARS_TOP_AWARD:
#     print('Congratulations! You are eligible for the Sales Manager Position.')
# else:
# # Multi-line with f-string
#     print(f'''
#     Sorry you do not meet the requirements for the Sales Manager Position.)

#     You need at least:
#     - {MIN_YEARS_SALES} years of ssales experience
#     - {MIN_YEARS_TOP_AWARD} years as salesperson of the year
#     ''')
