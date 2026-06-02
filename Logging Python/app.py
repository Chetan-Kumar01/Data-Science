import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("AirthmethicApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"Subtracting {a}-{b}={result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"Multiply {a}*{b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Divide {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    

add(10,3)
subtract(3,2)
multiply(8,9)
divide(20,0)