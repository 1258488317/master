#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
source = ['"D:\\text"']
#spaces in it.
target_dir='D:\\backup'
#target_dir='"F:\\biqiqi\\backup"'
#using
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
#zip_command="zip -qr {0} {1}".format(target ,' '.join(source))
#打开好压的EXE文件
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
zip_command = "makecab  \"%s\" \"%s\"" % (target, ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')