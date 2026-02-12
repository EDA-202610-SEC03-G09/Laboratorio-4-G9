from DataStructures.List import single_linked as lt
from DataStructures.Utils import error as error


def new_stack():
    try:
        return lt.new_list()
    except Exception as exp:
        error.reraise(exp, "TADStack->new_stack: ")


def push(my_stack, element):
    lt.add_last(my_stack, element)
    return my_stack

def pop(my_stack):
    if my_stack is not None and not lt.is_empty(my_stack):
        return lt.remove_last(my_stack)
    else:
        raise Exception

def is_empty(my_stack):
    return lt.is_empty(my_stack)

def top(my_stack):
    return lt.last_element(my_stack)

def size(my_stack):
    return lt.size(my_stack)
