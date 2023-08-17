from guidance import Vant
import logging

logging_filename = f'simple_test_guidance_class.log'
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, encoding='utf-8', level=logging.DEBUG)

vehicle = Vant(logging_filename)
vehicle.collect_info()

