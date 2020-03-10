import time

MP_BASE_URL = "http://ttapi.research.itcast.cn"
MP_HEADER = {"Content-Type": "application/json"}
MIS_BASE_URL = "http://ttapi.research.itcast.cn"
MIS_HEADER = {"Content-Type": "application/json"}
APP_BASE_URL = "http://ttapi.research.itcast.cn"
APP_HEADER = {"Content-Type": "application/json"}
import logging.handlers
def basic_logger_config():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    ls = logging.StreamHandler()
    filename= "../log/apiAutoTest_log_{}.text".format(time.strftime("%Y%m%d%H%M%M"))
    lht = logging.handlers.TimedRotatingFileHandler(filename=filename,when="midnight",interval=1,backupCount=2
                                                    )
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    logger.addHandler(ls)
    logger.addHandler(lht)