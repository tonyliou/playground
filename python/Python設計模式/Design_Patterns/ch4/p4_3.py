# p4_3.py
import logging
logging.basicConfig(level=logging.INFO)

def loggingDecorator(func):
    """記錄日誌的裝飾器"""
    def wrapperLogging(*args, **kwargs):
        logging.info("開始執行 %s() ..." % func.__name__)
        func(*args, **kwargs)
        logging.info("%s() 執行完成！" % func.__name__)
    return wrapperLogging

def showInfo(*args, **kwargs):
    print("這是一個測試函數，參數：", args, kwargs)

decoratedShowInfo = loggingDecorator(showInfo)
decoratedShowInfo('arg1', 'arg2', kwarg1 = 1, kwarg2 = 2)
