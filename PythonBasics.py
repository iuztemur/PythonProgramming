# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %% => bunun anlami bir section oldugunu gosterir ve bu sectionu run etmek icin Shift + Enter

#variables (degisken)
#functions
#objects
var1 = 10 #integer
var2 = 15
var3 = 10.0 #double or float
#5var = 10  #hata verir
gun = "pazartesi" #string

#variable lar standart conventon of python'a gore buyuk harfle baslamasi uygun degil.
#Comment ve tanimlamalarda turkce karakterler kullanilmaz.

#%%  => Ikinci Section 
#string 
s = "bugun gunlerden Pazartesi"

variable_type = type(s) #burada tanimlanan variable tipinin ne oldugunu ogreniriz. (str = string)

print(s)

var1 = "ankara"
var2 = "istanbul"
var3 = var1 + var2

print(var3)

uzunluk = len(var3)