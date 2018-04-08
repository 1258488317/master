#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
source=['"F:\\biqiqi\\document"', ' "F:\\biqiqi\\文档2"']
#spaces in it.
target_dir=r'"F:\biqiqi\backup'
#target_dir='"F:\\biqiqi\\backup"'
#using
target = target_dir+os.sep + time.strftime('%Y%m%d%H%M%S' + '.zip') + '"'
#zip_command="zip -qr {0} {1}".format(target ,' '.join(source))
zip_command = r"C:\QMDownload\SoftMgr\haozip_v5.9.7-5.9.7.10871.exe a %s %s" %(target, ' '.join(source))
print(zip_command)
if os.system(zip_command) == 0 :
    print('Successful backup to',target)
else:
    print('失败')
