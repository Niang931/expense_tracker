import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('security/app.log',
                                   mode='a', encoding='utf-8')
file_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

