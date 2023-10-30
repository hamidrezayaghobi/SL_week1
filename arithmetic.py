from .logger import log_str

def subtract(x, y, logger=log_str):
    if monitor:
	logger(f'x = {x}, y = {y}')
    return 1.0 * x - y
def add(x, y, logger=log_str):
    if monitor:
        logger(f'x = {x}, y = {y}')
    return 1.0 * x + y

def multiply(x, y, logger=log_str):
    if monitor:
        logger(f'x = {x}, y = {y}')
    return 1.0 * x *  y

def divide(x, y, logger=log_str):
    if monitor:
        logger(f'x = {x}, y = {y}')
    if y == 0:
	raise "division by zero"
    return 1.0 * x / y
