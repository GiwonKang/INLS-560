import re

# Dictionary of random names and phone numbers
contacts = {
    'Smith, John': '919-555-1234',
    'Doe, Jane': '919-555-5678',
    'Johnson, Emily': '919-555-8765',
    'Brown, Michael': '919-555-4321',
    'Wilson, Sarah': '919-555-9999',
    'Taylor, David': '202-555-0123',
    'Anderson, Linda': '303-555-9876',
    'Thomas, Chris': '404-555-3456',
    'Jackson, Karen': '512-555-2345',
    'White, Daniel': '718-555-6543',
    'Harris, Patricia': '213-555-7890',
    'Martin, Robert': '415-555-1122',
    'Thompson, Michelle': '214-555-9988',
    'Garcia, James': '305-555-6655',
    'Martinez, Laura': '602-555-4433',
}

pattern = r'919'
count_919 = 0
count_non_919 = 0

for name, phone in contacts.items():
    if re.search(pattern, phone):
        print(f'{name} with phone {phone} contains the pattern {pattern}')
        count_919 += 1
    else:
        print(f'The pattern "{pattern}" is not in the phone number for {name}.')
        count_non_919 += 1

# Calculate the total and percentage
total_contacts = len(contacts) # Lengths of the contact
percentage_919 = (count_919 / total_contacts) * 100 if total_contacts > 0 else 0

print(f'\nTotal count of non-919 phone numbers: {count_non_919}')
print(f'Total count of 919 phone numbers: {count_919}')
print(f'Percentage of 919 phone numbers: {percentage_919:.2f}%')