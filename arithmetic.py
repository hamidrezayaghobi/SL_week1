def subtract(x, y):
    return float(x) - float(y)

def add(x, y):
    return float(x) + float(y)

def multiply(x, y):
    return float(x) * float(y)

def divide(x, y):
    if y == 0:
	raise "division by zero"
    return float(x) / float(y)
