import logging

logging.basicConfig(level=logging.INFO)   #my_logger.setLevel(logging.INFO)
logger = logging.getLogger("my_logger")

try:
    1 / 2
except ZeroDivisionError as e:
    logger.exception("Произошла ошибка деления на ноль")



#######################################
def first_func():
    second_func()

def second_func():
    third_func()

def third_func():
    raise Exception("Произошла ошибка в функции third_func()")


try:
    first_func()
except Exception:
    logger.exception("Произошла ошибка деления на ноль", exc_info=True)

