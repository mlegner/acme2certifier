#/usr/bin/python3
# import threading
from acme_srv.threadwithreturnvalue import ThreadWithReturnValue
import logging
import time

def my_main(logger):

    logger.debug('my_main: threat initialize')

    twrv = ThreadWithReturnValue(target=my_func, args=(logger, 12, 'bar'))
    twrv.start()
    result = twrv.join(timeout=5)

    return result

def my_func(logger, arg1, arg2):
    logger.debug('Thread: my_func started')
    logger.debug('Thread: args: {0}, {1}'.format(arg1, arg2))
    time.sleep(arg1)
    logger.debug('Thread: my_func ended')

    return ('jepp', 'yeapp', 'yoah')

if __name__ == '__main__':

    logging.basicConfig(
        format="%(asctime)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG)
    logger = logging.getLogger('acme2certifier')

    logger.debug('main: start')
    result = my_main(logger)

    if result:
        myresult = result
    else:
        myresult = 'timeout'

    logger.debug('main: end with: {0}'.format(myresult))
    print('nextnext')
