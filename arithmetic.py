def subtract(x, y):
    return 1.0 * x - y
def add(x, y):
    return 1.0 * x + 1.0 * y

def multiply(x, y):
    return 1.0 * x * y

def divide(x, y):
    if y == 0:
	raise "division by zero"
    return 1.0 * x / y
