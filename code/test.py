# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:49:31 2020

@author: 86178
"""

import sys

score = 100

with open('./high_score.txt','w') as f:
    f.write(str(score))
with open('./high_score.txt','r') as f:
    print(int(f.read()))