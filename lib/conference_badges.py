def badge_maker(name):
    badge = f'Hello, my name is {name}.'
    return badge

def batch_badge_creator(names):
    l = []
    for name in names:
        l.append(f'Hello, my name is {name}.')
    return l

def assign_rooms(names):
    l = []
    index = 0
    while index < 8:
        l.append(f"Hello, {names[index]}! You'll be assigned to room {index + 1}!")
        index += 1
    return l

def printer(names):
    for output in batch_badge_creator(names):
        print(output)
    for output in assign_rooms(names):
        print(output)
    return None
