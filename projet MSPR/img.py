# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:17:53 2023

@author: Thuy-trang
"""

import os
path = "C:/Users/Thuy-trang/Downloads/1a76c251-8cf1-476b-a8e1-1ec19ccab6ed"
imgs = os.listdir(path)
for img in imgs :
    if "cat" not in img : 
        os.remove(path + "/" + img)
        

