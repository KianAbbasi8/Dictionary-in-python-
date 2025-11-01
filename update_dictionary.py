
#syntax for updated only the existing element:

my_dict={

"name":"ali", "caste":"abbasi"
}
#syntax
my_dict["name"]="muddassar"
print(my_dict)
print("=========================================")
#get
gets=my_dict.keys()
print(gets)
print("=========================================")
#pop
popp=my_dict.pop("caste")
print(popp)
print(my_dict)
#remove last element:
print("=========================================")

removed=my_dict.popitem()
print(removed)
print(my_dict)
print("=========================================")
clean=my_dict.clear()
print(clean)
print("=========================================")
valus=my_dict.values()
print(list(valus))