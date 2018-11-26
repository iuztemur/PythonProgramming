# Python Basics Begin
# Tis script includes(Variables, String, Numbers, Built In, User Defined, Default, Flexible Function, Lambda Function
#  and Quiz1(Quiz1.py))
# Author Ismail Uztemur

# %% => bunun anlami bir section oldugunu gosterir ve bu sectionu run etmek icin Shift + Enter

# %% Variables -> Section 1

# variables(degisken)
# Functions
# Objects

var1 = 10  # integer
var2 = 15
var3 = 10.0  # double or float (ondalikli rakamlar.)
# 5var = 10  #hata verir

gun = "pazartesi"
# string

# variable lar standard convention of python'a gore buyuk harfle baslamasi uygun degil.
# Comment ve tanimlamalarda turkce karakterler kullanilmaz.



# %% String => Section 2

s = "bugun gunlerden pazartesi"

variable_type = type(s)  # burada tanimlanan variable tipinin ne oldugunu ogreniriz. (str = string)

print(s)

var1 = "ankara"
var2 = "ist"
var3 = var1 + var2

var4 = "100"
var5 = "200"
var6 = var4 + var5

uzunluk = len(var6)



# %% Numbers -> Section 3

# int
integer_deneme = -50
# double = float = ondalikli sayi
float_deneme = -30.7



# %% Built In Functions -> Section 4

# Build in functions: Programlama dili tafindan daha onceden tanimlanmis olan fonksiyonlara denir.

str1 = "deneme"
float1 = 10.6
# float(10)
# int(float1)  Burada float'i int degere cevirir.
# round(float1) Burada float1 degerini 11'e yuvarlıyor.
str2 = "1005"  # int(str2) => string bir degeri int bir degere ceviriyor. # type(int(str1)) => donusturulen degerin degisken tipini verir.

# output = type(parameter(input))



# %% User Defined Functions -> Section 5

# User defined functions: Programci tafindan yazılan fonksiyonlara denir.
# Bu tur fonk. bir ilem tekrar edecekse bunu defalarca copyalayıp yazmak yerine bir fonk. ile tanimlayip tekrar takrar cagrilmasidir.
# def(definition) anahtar kelimesi ile ifade edilir.

var1 = 20
var2 = 50

output = (((var1 + var2) * 50) / 100.0) * var1 / var2


# fonksiyon parametresi = input
def benim_ilk_func(a, b):
    """
    ilk fonksiyon denemem
    Fonksiyon blogunun icini doldurulurken bir sonraki satıra tab ile baslanir bu da python'in formatidir.
    parametre:

    return:
    """
    output = (((a + b) * 50) / 100.0) * a / b

    return output


sonuc = benim_ilk_func(var1, var2)


def deneme1():
    print("Bos fonksiyon denemesi")


    
# %% Default and Flexible Functions -> Section 6

# Cember cevres hesaplayan bir fonksiyon.

# default function: cemberin cevre uzunlugu = 2*pi*r

def cember_cevresi_hesapla(r, pi=3.14):
    """
    cember cevresi hesapla
    input(parametre): r,pi
    output = cemberin cevresi
    """

    output = 2 * pi * r
    return output


# flexible function

# def hesapla(boy,kilo,yas):
#    output = (boy+kilo)*yas
#    return output

# *args => bunun anlami biz fonk. parametresine ister bir veya birden fazla param. ekleriz ya da hic eklemeyiz.

def hesapla(boy, kilo, *args):
    print(len(args))  # arg => uzunlugunu verir, hic birsey yazmazsak 0 gelir.
    output = (boy + kilo) * args[0]
    return output


  
# %% QUIZ

# int variable yas
# string name isim
# fonksiyonu olacak
# fonksiyon print(type(),len,float())
# *args soyisim
# default parametre ayakkabi numarasi

yas = 27
name = "ismail"
soyisim = "uztemur"


def function_quiz(yas, name, *args, ayakkabi_numarasi=44):
    print("Cocugun ismi: ", name, " yasi: ", yas, " ayak numarasi: ", ayakkabi_numarasi)
    print(type(name))
    print(float(yas))

    output = args[0] * yas

    return output


sonuc = function_quiz(yas, name, soyisim)

print("args[0]*yas: ", sonuc)



# %%
# Lambda Function -> Section 7

def hesapla(x):
    return x * x


sonuc = hesapla(3)

sonuc2 = lambda x: x * x
print(sonuc2(3))



# %%
# List -> Section 8
# Cok fazla data store edilirken kullanila bilir.

liste = [1,2,3,4,5,6]
type(liste)

liste_str = ["ptesi","sali","cars"]
type(liste_str)

value = liste[1] # Listenin Ilk elamanini getirir.
print(value)

last_value = liste[-1] # Listenin Son Elamanini Getirir.

liste_divide = liste[0:3] # Listenin belirlenmiş elemanlarini 

liste.append(7) # Bir listenin en sonuna bir elaman ekler
liste.remove(7) # Bir listeden elaman cıkarır
liste.reverse(7) # Listeyi ters çevirir.
liste2 = [1,5,4,3,6,7,2]
liste2.sort() # Listenin elemanlarını sıralar.

string_int_liste = [1,2,3,"aa","bb"]



# %%
# Tuple -> Section 9 
# dir(tuple) kullanilan fonksiyonlarini gösterir.dir
# help(tuple.funk.) fonk. elamanlarinin nasil kullanildigini gosterir.

t = (1,2,3,3,4,5,6)

t.count(3) # count icinde yazilan elemanin listedeki kullanim sayisini verir.
t.index(3) # index icindeki elemanin kullaildigi indexi gosterir.



# %% Dictionary -> Section 10
# Local databaseler icin dictionary kullanmak veya multiple return yaparken kullanmak daha iyi

dictionary = {"ali": 32, "ahmet": 38, "ayse":15}

# ali, ahmet, ayse = keys
# 32,45,13 = values

def deneme():
    dictionary = {"ali": 32, "ahmet": 38, "ayse":15}
    return dictionary

dic = deneme()



# %% Conditionals -> Section 11
# if else statement, else statement tan sonra daima  ':' ile islemi sonlandirmak gerekiyor.

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 buyuktur var2")
elif(var1 == var2):
    print("var and var2 esitler")
else:
    print("var1 kucuktur var2")


liste = [1,2,3,4,5]

value = 3
if value in liste:
    print("evet {} degeri listenin icinde".format(value))
else:
    print("hayir")


keys = dictionary.keys()

if "can" in keys:
    print("evet")
else:
    print("hayir")
































































