# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:17:53 2023

@author: Thuy-trang
"""

import os
path = "C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/Mammifères/Lapin/7fea0f24-799b-4c2a-b051-eb51290598b8"
imgs = os.listdir(path)
for img in imgs :
    if "rabbit" not in img : 
        os.remove(path + "/" + img)
        

