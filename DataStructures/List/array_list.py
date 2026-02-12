def new_list():
    newlist = {
        "elements":[],
        "size":0
    }
    return newlist


def  get_element(my_list, index):
    if index < 0 or index >= size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][index]

def is_present(my_list, element,cap_function):
    
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list['elements'][keypos]
            if cap_function( element, info) == 0:
                keyexist = True
                break
            if keyexist:
                return keypos
    return -1

def add_first(my_list, element):
    my_list['elements'].insert(0,element)
    my_list['size'] += 1
    return my_list
def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list

def size(my_list)-> int:
    return my_list['size']

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][0]

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list['elements'][my_list['size']-1]

def is_empty(my_list):
    if my_list['size'] == 0:
        return True
    else:
        return False
    
def delete_element(my_list, index):
    if index < 0 or index >= size(my_list):
        raise Exception('IndexError: list index out of range')
    if index < my_list['size']:
        del my_list['elements'][index]
        my_list['size'] -= 1
    return my_list


def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    removed = my_list['elements'][0]
    del my_list['elements'][0]
    my_list['size'] -= 1
    return removed

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    removed = my_list['elements'][my_list['size']-1]
    del my_list['elements'][my_list['size']-1]
    my_list['size'] -= 1
    return removed
def insert_element(my_list, index, element):
    my_list['elements'].insert(index, element)
    my_list['size'] += 1
    return my_list

def change_info(my_list, index, element):
    if index < 0 or index >= size(my_list):
        raise Exception('IndexError: list index out of range')
    my_list['elements'][index] = element
    return my_list

def exchange(my_list, index1, index2):
    if index1 < 0 or index1 >= size(my_list) or index2 < 0 or index2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    temp = my_list['elements'][index1]
    my_list['elements'][index1] = my_list['elements'][index2]
    my_list['elements'][index2] = temp
    return my_list

def sub_list(my_list, index, num_elements):
    if index < 0 or num_elements < 0 or index + num_elements > size(my_list):
        raise Exception('IndexError: list index out of range')

    sublist = new_list()

    for i in range(index, index + num_elements):
        add_last(sublist, my_list['elements'][i])

    return sublist