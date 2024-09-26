from sys import getsizeof

# NOTE:
# when using the yield keyword the function gets called everytime it's iterated over in the loop
# The function below is an example of a generator
def my_range(n: int):
    print('my_range loop starts')
    start = 0
    while start < n:
        print(f'my_range is returning: {start}')
        yield start
        start += 1

# big_range = range(1000)
big_range = my_range(5)

print(next(big_range))
big_range_bytes = f'big_range is {getsizeof(big_range)} bytes'

# populate big_range list
big_list = []
for val in big_range:
    big_list.append(val)


big_list_bytes = f'big_list is {getsizeof(big_list)} bytes'


# A very simaple example of yield
def show_yield():
    yield 2
    yield 4
    yield 6
    yield 8

show_yield_var = show_yield()

print(f'show_yeild next result => {next(show_yield_var)}')

for n in show_yield_var:
    print(n)

def main():
    print(big_range_bytes)
    print(big_list_bytes)
    print(big_range)
    print(big_list)

if __name__ == '__main__':
    main()
