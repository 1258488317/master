#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
#建立一个filehandler来把日志记录在文件里，级别为debug以上
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
#建立一个streamhandler来把日志打在cmd窗口上。级别为error以上
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
#设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
#将对应的handler添加到logger对象中
logger.addHandler(ch)
logger.addHandler(fh)
#开始打日志
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")