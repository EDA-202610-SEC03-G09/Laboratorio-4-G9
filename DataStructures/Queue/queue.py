from DataStructures.List import single_linked_list as al
from DataStructures.Utils import error as error

def new_queue():
    try:
        return al.new_list()
    except Exception as exp:
        error.reraise(exp, 'TADQueue->new_queue: ')

def enqueue(my_queue, element):
    x=al.add_last(my_queue, element)
    return x

def dequeue(my_queue):
    return al.remove_first(my_queue)


def peek(my_queue):
    return al.first_element(my_queue)


def is_empty(my_queue):
    return al.is_empty(my_queue)


def size(my_queue):
    return al.size(my_queue)

