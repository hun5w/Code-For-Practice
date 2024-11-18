def hello_1(greeting, name):
    print('{}, {}!'.format(greeting, name))

hello_1(greeting = 'Hello',name ='world')
hello_1(name = 'world', greeting ='Hello')

def print_params(*params):
    print(params)

print_params('Testing')
print_params(1, 2, 3)

def prepare_for_party(main_gift, *gifts):
    print('The main gift is:', main_gift)
    print('The other gifts are:', gifts)

prepare_for_party('cake', 'candles', 'presents', 'music')