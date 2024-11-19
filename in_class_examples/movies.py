#Import the regular expression module. 

import re

films = ['hellraiser', 'it', 'nightmare on elm street', 'c.h.u.d.',
         'alien', 'nosferatu', 'halloween', 'jaws', 'e.t.', 'poltergeist']

intro_line = 'here is a list of fun movies to watch this Halloween season:'

# Print the intro line capitalized
print(intro_line.capitalize())

# Regex pattern to match titles with periods so that they will be capitalized.
pattern = r'\.' # the . must be escaped. \. for string, . for directory

for movie in films:
    if re.search(pattern, movie):
        print(movie.upper())
    else:
        print(movie.title())