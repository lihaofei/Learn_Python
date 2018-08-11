#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bill Li
def add(a,b,f):
    return f(a)+f(b)

l=add(1,-4,abs)
print(l)