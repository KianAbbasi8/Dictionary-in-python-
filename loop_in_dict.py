profile={

    "name ":"ali","status":"student","university":"IBA","gender":"male "

}
print("===================print keys only======================")
#print only key using loop
for k in profile:
    print(k)
    
print("====================values=====================")
for j in profile.values():
    print(j)
print("================= both key and value ========================")
for total in profile.items():
    print(total)