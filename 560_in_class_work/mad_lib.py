# Mad lib example for functions.

def madlib(noun_1, verb_1, noun_2, adjective_1, noun_3, verb_2, adjective_2, verb_3):
    '''Mad lib function'''

    story = f'''
In a world filled with mystery and magic, Doctor Strange, once a skilled {noun_1}, found his life turned upside down after a terrible accident. His hands, once steady, could no longer {verb_1} with precision, leaving him desperate for answers. He sought out the Ancient One, hoping to find a way to heal his {noun_2} and return to his former life.

The Ancient One revealed to Strange the vast and {adjective_1} world of mysticism, showing him that the universe was more than just physical {noun_3} and material things. Through intense training and meditation, Doctor Strange learned to {verb_2} portals, manipulate time, and wield magic like no other. However, he quickly realized that the powers he sought were not just for personal gain, but to protect the world from the forces of darkness.

Armed with the {adjective_2} Cloak of Levitation, Doctor Strange faced off against powerful enemies like Dormammu, using every bit of his knowledge and magic to {verb_3} them. His journey from a self-centered surgeon to the Sorcerer Supreme was not just about learning magic, but about understanding his role in protecting all of reality.
'''

    return story

output_story = madlib('cat', 'eat', 'orange', 'slowly', 'curtain', 'sleep', 'largely', 'drink')
print(output_story)