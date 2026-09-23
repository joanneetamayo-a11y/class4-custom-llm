"""Write original practice material outside corpus until the baseline is saved.

No eval file, answer list, or output is read by this generator.
"""
from pathlib import Path

destination = Path('teaching_drafts')
destination.mkdir(exist_ok=True)
sequence = []
activities = [
    ('peel the orange', 'slice the orange'),
    ('open the jar', 'fill the bowl'),
    ('buy a ticket', 'board the train'),
    ('wash the plate', 'dry the plate'),
    ('read the recipe', 'bake the bread'),
    ('pack the bag', 'leave the house'),
    ('draw a picture', 'paint the picture'),
    ('unlock the gate', 'enter the garden'),
    ('write a letter', 'mail the letter'),
    ('plant a seed', 'water the soil'),
    ('turn on the light', 'read the book'),
    ('put on shoes', 'walk outside'),
]
for first, second in activities:
    sequence.extend([
        f'First {first}; next {second}. The final task is to {second}.',
        f'Before you {second}, {first}. The earlier task is to {first}.',
        f'After you {first}, {second}. The later task is to {second}.',
        f'Two actions are planned: {first}, then {second}. Start by choosing to {first}.',
        f'The last task is to {second}. The first action is to {first}.',
    ])
for early, late in [('breakfast','dinner'), ('lunch','supper'), ('practice','the concert'),
                    ('sunrise','sunset'), ('the lesson','the quiz'), ('the game','the celebration')]:
    sequence.extend([
        f'{early} comes before {late}. Of these events, {late} is later.',
        f'{late} follows {early}. Of these events, {early} is earlier.',
        f'We finish {early} and then begin {late}. The second event is {late}.',
    ])
for early, late in [('taxi','bicycle'), ('car','train'), ('bus','truck'), ('boat','car'), ('truck','taxi')]:
    sequence.extend([
        f'At the station a {early} arrived first and a {late} arrived second. The {early} was early.',
        f'At noon the {late} arrived after a {early}. The {late} was the later arrival.',
        f'A {early} left before a {late}. The first vehicle to leave was a {early}.',
    ])

spatial = []
for obj, container in [('coin','cup'), ('pencil','drawer'), ('key','bag'), ('book','box'),
                       ('apple','basket'), ('toy','cabinet'), ('shoe','chest'), ('letter','envelope')]:
    spatial.extend([
        f'A {container} contains a {obj}. The {obj} rests inside this {container}.',
        f'Look inside this {container} to find a {obj}. This container holds the {obj}.',
        f'We put a {obj} into a {container}. Now the {obj} is inside.',
        f'A {obj} was taken out of a {container}. It is now outside the {container}.',
    ])
for high, low in [('shelf','chair'), ('clock','desk'), ('lamp','rug'), ('picture','sofa'),
                   ('bird','tree'), ('window','bench'), ('basket','table'), ('mirror','sink')]:
    spatial.extend([
        f'Above a {low} hangs a {high}. The {low} sits below the {high}.',
        f'Below a {high} stands a {low}. The {high} is higher than the {low}.',
        f'The {low} is under the {high}, not above it.',
        f'Place a {high} over the {low}. The lower object is the {low}.',
    ])
for left, right in [('cup','plate'), ('ball','shoe'), ('book','lamp'), ('bag','chair'),
                    ('desk','shelf'), ('box','basket'), ('tree','bench'), ('car','bus')]:
    spatial.extend([
        f'Place the {left} on the left and the {right} on the right. The {right} is beside the {left}.',
        f'To the right of a {left} sits a {right}. To the left of that {right} sits the {left}.',
        f'The {right} has a {left} on its left side. The {left} has the {right} on its right side.',
    ])
spatial.extend([
    'A map shows north at the top and south at the bottom.',
    'The school is north of the park. Going south from the school leads to the park.',
    'The bank is south of the market. Travel north from the bank to reach the market.',
    'Beside means next to something. A chair can stand beside a desk.',
])
for name, passages in [('sequence.txt', sequence), ('spatial_relations.txt', spatial)]:
    assert len(passages) == len(set(passages))
    (destination / name).write_text('\n'.join(passages) + '\n')
    print(name, len(passages), 'original teaching lines')
