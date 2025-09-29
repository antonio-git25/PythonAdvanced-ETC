import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("devide_log.log")
stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#logger.error("Error is appear")


def division():
    logger.debug("Начало выполнения деления!")
    try:
        dividend = float(input("Введите делимое: "))
        divisor = float(input("Введите делитель: "))
    except ValueError:
        logger.log(logging.CRITICAL, "Введены не числовые значения")
    except ZeroDivisionError:
        logger.error("Деление на ноль")
    else:
        logger.info(f"Получен результат {dividend / divisor} в процессе деления {dividend} на {divisor}")
        return dividend / divisor


res = division()
print(res)