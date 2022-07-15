import random

def bool_to_str(bool):
    if bool is None:
        return 'X'
    elif bool is True:
        return '1'
    else:
        return '0'

def rand_bool_none():
    i = random.randrange(3)
    if i == 0:
        return True
    elif i == 1:
        return False
    else:
        return None

def rand_bool():
    return random.choice([True, False])

def group_num_to_group_tuple(group_num, num_groups):
    group_tuple = [ None ] * num_groups
    group_tuple[group_num] = True
    return tuple(group_tuple)