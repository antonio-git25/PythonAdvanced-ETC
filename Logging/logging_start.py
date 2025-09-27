import logging

def print_looger_nums():
    print("\n")
    print(logging.NOTSET)  # 0
    print(logging.DEBUG)  # 10
    print(logging.INFO)  # 20
    print(logging.WARNING)  # 30
    print(logging.ERROR)  # 40
    print(logging.CRITICAL)  # 50
    print("\n")


def print_log_level():
    logging.debug("Это сообщение уровня DEBUG")
    logging.info("Это сообщение уровня INFO")
    logging.warning("Это сообщение уровня WARNING")
    logging.error("Это сообщение уровня ERROR")
    logging.critical("Это сообщение уровня CRITICAL")


##################################################################


logging.basicConfig(level=logging.DEBUG)
my_logger = logging.getLogger("my_logger")

my_logger.debug("Это сообщение уровня DEBUG")
my_logger.info("Это сообщение уровня INFO")
my_logger.warning("Это сообщение уровня WARNING")
my_logger.error("Это сообщение уровня ERROR")
my_logger.critical("Это сообщение уровня CRITICAL")

my_logger.setLevel(logging.INFO)
my_logger.info("INFO Изменили уровень логирования")

my_logger.debug("Это сообщение уровня DEBUG - его все еще не видно")
my_logger.info("Это сообщение уровня INFO")
my_logger.warning("Это сообщение уровня WARNING")
my_logger.error("Это сообщение уровня ERROR")
my_logger.critical("Это сообщение уровня CRITICAL")