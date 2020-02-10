def hello_func(greeting, name='You'):
    return'{}, {}'. format(greeting, name)


print(hello_func('Hi', name = 'Farhana').upper())

# args for touples kwargs for dictionary
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Farhana', Age=26)