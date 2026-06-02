from my_logger import logging  # also fine if you want direct access to logging

def add(a,b):
    logging.debug("The addition operation is taking place")
    return a+b

logging.debug("The addition is succesful")
add(10,4)