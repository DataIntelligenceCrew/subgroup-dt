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

def argmax2(collection):
    maximizer = None
    max_value = None
    for i in range(len(collection)):
        if maximizer is None or collection[i] > max_value:
            maximizer = i
            max_value = collection[i]
    return maximizer

def argmax(collection, function):
    maximizer = None
    max_value = float('-inf')
    for item in collection:
        if maximizer is None or function(item) > max_value:
            maximizer = item
            max_value = function(item)
    return maximizer

def argmin(collection, function):
    def maximizer_function(item):
        return -1 * function(item)
    return self.argmax(collection)

def maximum(collection, function):
    max_value = float('-inf')
    for item in collection:
        if function(item) > max_value:
            max_value = function(item)
    return max_value

def minimum(collection, function):
    min_value = float('inf')
    for item in collection:
        if function(item) < min_value:
            min_value = function(item)
    return min_value