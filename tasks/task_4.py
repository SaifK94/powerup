"""
Task 4: Dictionaries, aka `dict`

- are you familiar and confident with: `strings` and `ints`
- are you familiar and confident with: `lists` and `dictionaries`
- are you familiar and confident with: `functions`

=======
Brief:

See if you can build a dictionary of 5 people, with their ages,
best time in mario kart and height.

Then, print the:
- tallest,
- oldest and/or
- person with the fastest time

"""
import pprint

Racers = [
    {'name': 'Daniel',
     'age': 34,
     'best time': '03:43',
     'height': '178cm'
     },
    {'name': 'Saif',
     'age': 28,
     'best time': '03:15',
     'height': '173cm'
     },
    {'name': 'Kai',
     'age': 25,
     'best time': '03:27',
     'height': '170cm'
     },
    {'name': 'Isaac',
     'age': 23,
     'best time': '03:34',
     'height': '180cm'
     },
    {'name': 'Liam',
     'age': 32,
     'best time': '03:50',
     'height': '183cm'
     }
]
# pprint.pprint(sorted(Racers, key=lambda x: x['age']))
print('Tallest Racer')
print(max(Racers, key=lambda x: x['height'])['name'])
print(max(Racers, key=lambda x: x['height'])['height'])
print('Youngest Racer')
print(min(Racers, key=lambda x: x['age'])['name'])
print(min(Racers, key=lambda x: x['age'])['age'])
print('Fastest Racer')
print(min(Racers, key=lambda x: x['best time'])['name'])
print(min(Racers, key=lambda x: x['best time'])['best time'])