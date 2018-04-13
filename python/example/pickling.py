#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple','mango','bannana']

f = open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close()

del shoplist
f = open(shoplistfile,'rb')
storedlist = pickle.load(f)
print(storedlist)