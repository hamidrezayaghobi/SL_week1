def subtract(x, y, monitor=False):
    if monitor:
	print(f'x = {x}, y = {y}')
    return 1.0 * x - y
def add(x, y, monitor=False):
    if monitor:
        print(f'x = {x}, y = {y}')
    return 1.0 * x + y

def multiply(x, y, monitor=False):
    if monitor:
        print(f'x = {x}, y = {y}')
    return 1.0 * x *  y

def divide(x, y, monitor=False):
    if monitor:
        print(f'x = {x}, y = {y}')
    if y == 0:
	raise "division by zero"
    return 1.0 * x / y
