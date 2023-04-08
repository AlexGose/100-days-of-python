
def get_names():
    with open('Input/Names/invited_names.txt') as names:
        lines = names.readlines()
    return [line.strip() for line in lines]


def create_letter(name):
    with open('Input/Letters/starting_letter.txt') as template:
        lines = template.readlines()
    lines[0] = lines[0].replace('[name]', name)
    with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as letter:
        letter.writelines(lines)


for invitee in get_names():
    create_letter(invitee)
