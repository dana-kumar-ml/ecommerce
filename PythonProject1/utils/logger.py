# utils/logger.py
import logging
import os

def setup_logger(name="test_logger", log_file="logs/test.log"):
    os.makedirs("logs", exist_ok=True)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger
