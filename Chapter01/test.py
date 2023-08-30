#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ************************************************************************ 
# * 
# * @file:test.py 
# * @author:nanjingrjb@gmail.com 
# * @date:2023-08-30 23:21 
# * @version 1.0  
# * @description: Python Script 
# * @Copyright (c)  all right reserved 
# * 
#************************************************************************* 

import os,sys
from price_log import PriceLog
log = '[2023-08-31T06:58:21.567891] - SALE - PRODUCT:989 - PRICE:$50.56'    
PriceLog.parse(log)

