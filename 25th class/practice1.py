# data = "BP:120/80  HR=72% Temp=38.9C Sugar-155mg Chol=190mg HDL=45mg LDL=110mg"

# bp = data[data.index("BP:")+3 : data.index("HR")].strip()
# systolic , diastolic = [int(x) for x in bp.replace("HR","").split("/")]

# hr_str = data[data.index("HR=")+3 : data.index("%")]
# HR = int(hr_str)

# temp_str = data[data.index("Temp=")+5 : data.index("C")]
# temp = float(temp_str)

# sugar = int(data[data.index("Sugar-")+6 : data.index("mg")])
# chol = int(data[data.index("Chol=")+5 : data.index("mg", data.index("Chol="))])
# hdl = int(data[data.index("HDL=")+4 : data.index("mg", data.index("HDL="))])
# ldl = int(data[data.index("LDL=")+4 : data.index("mg", data.index("LDL="))])



# print( " BP = " , systolic,"/",diastolic , "\n" ,"HR = " ,  hr_str,"%","\n" ,"Temp = " ,  temp,"C","\n" , "Sugar-", sugar,"mg" ,"\n", "Chol = " , chol,"mg" , "\n" , "HDL = ", hdl,"mg" , "\n" , "LDL = " , ldl,"mg" )


data = "Chol=190mg HDL=45mg LDL=110mg"

chol = int(data[data.index("Chol=")+5: data.index("mg")])
hdl = int(data[data.index("HDL=")+4 : data.index("mg", data.index("HDL="))])
ldl = int(data[data.index("LDL=")+4 : data.index("mg", data.index("LDL="))])

print(" Chol = " , chol,"mg" , "\n" , "HDL = ", hdl,"mg" , "\n" , "LDL = " , ldl,"mg" )


chol_mmol = chol * 0.0259
hdl_mmol = hdl * 0.0259

print("Chol_mmol =  " , chol_mmol , "\n" , "Hdl = " ,round(hdl_mmol, 2.))