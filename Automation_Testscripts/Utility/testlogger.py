import logging

class Testgetlogger():
    def test_log(self):
    # Create a FileHandler
        logger = logging.getLogger('my_logger')
        file_handler = logging.FileHandler('my_log_file.log')
        formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

    # Set the logging level
        logger.setLevel(logging.DEBUG)

    # Create a logger and add the FileHandler to it
        logger.addHandler(file_handler)
        return logger