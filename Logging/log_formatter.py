import logging

logging.basicConfig(level=logging.DEBUG, encoding="utf-8")
logger = logging.getLogger("my_logger")

file_handler = logging.FileHandler("test_out.txt")
stream_handler = logging.StreamHandler()
logger.addHandler(file_handler)
#logger.addHandler(stream_handler)

logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")