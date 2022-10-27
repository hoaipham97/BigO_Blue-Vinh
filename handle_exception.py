import traceback
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='app_logging.log',
                    filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

try:
    a = 5/1
    val = 6
except ZeroDivisionError as e:
    logging.error(' error is %s', e)
except Exception as e:
    logging.error('Cannot get value cause: ', e)
else:
    logging.info('Success')
finally:
    logging.info('Clean up...')