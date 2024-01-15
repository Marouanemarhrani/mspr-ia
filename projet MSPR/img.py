# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:17:53 2023

@author: Thuy-trang
"""

import os
path = "C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/Mammifères/Ecureuil/0ef6a4e9-7e1f-492b-9371-7397dc090ae4"
imgs = os.listdir(path)
for img in imgs :
    if "squirrel" not in img : 
        os.remove(path + "/" + img)
        

