def subtract(x, y, monitor=False):
    if monitor:
	print(f'x = {x}, y = {y}')
        return float(x) - float(y)
    return float(x) - float(y)
def add(x, y, monitor=False):
    if monitor:
        print(f'x = {x}, y = {y}')
        return float(x) + float(y)
    return float(x) + float(y)

def multiply(x, y, monitor=False):
    if monitor:
        print(f'x = {x}, y = {y}')
        return float(x) * float(y)
    return float(x) * float(y)

def divide(x, y, monitor=False):
    if monitor:
        print(f'x = {x}, y = {y}')
	if y == 0:
            raise "division by zero"

        return float(x) /  float(y)

    if y == 0:
	raise "division by zero"
    return float(x) / float(y)
