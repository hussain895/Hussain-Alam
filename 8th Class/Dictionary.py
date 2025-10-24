Dic = {1:"ALI",2:"HUSSAIN",3:"MURTAZA",4:"MEASUN",5:"DANIYAL" }
print(Dic)

Dict =dict({1:"ALI",2:"HUSSAIN",3:"MURTAZA",4:"MEASUN",5:"DANIYAL" })
print(Dict)

print(Dict[2])
print(Dict[3])
print("\n")



mydict = {}
mydict[0]="Python"
mydict[2]="Hussain"
mydict[3]="Murtaza"
print(mydict)

mydict["Value_set"]=1,2,3
print(mydict)

mydict[4] = {'Nested':{'1':'Measum' , '2': 'Daniyal' } }
print(mydict)
print(mydict.get(4))
print(mydict.get(3))
print(mydict[4]['Nested'])
print("\n")

dict_deep = dict(Dict)
print(dict_deep)
dict_deep['a'] = 10
print(dict_deep)
print(Dict)
print("\n")

dict_shallow = Dict
print(dict_shallow)
dict_shallow['c'] = 11
print(dict_shallow)
print(Dict)
print("\n")

text1 = {1 : 'Hussain' , 2 : 'Murtaza'}
text2 = text1

text1.clear()
print("text1 = ",text1)
print("text2 = ",text2)
print("\n")

text3 = {1 : 'Measun' , 2 : 'Ali'}
text4 = text3

text3= {}
print("text3 = ",text3)
print("text4 = ",text4)
print("\n")



dict1 = {1 : 'abc' , 2 : 'xyz'}
dict2 = dict1.copy()
print('New Copy' , dict2)
dict2[3] = 10
dict2[10] = 30
print("Updated Copy : " , dict2)