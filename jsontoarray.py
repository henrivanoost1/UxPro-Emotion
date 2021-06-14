import json

with open("test1.json", 'r+') as file:
    to_python= json.loads(file.read())

    array_keys= to_python.keys()
    array_keys1= str(array_keys)
    array_keys2= array_keys1.replace("([","")
    array_keys3=array_keys2.replace("])","")
    array_keys4=array_keys3.replace("dict_keys","")
    array_keys5=array_keys4.replace("'","")
    # array_keys5=array_keys5.replace("'","")
    array_keys5= array_keys5.split(",")

    time_start= float(array_keys5[0])
    time_end=float(array_keys5[len(array_keys5)-1])

    time_calc=time_end-time_start

    for i in range(len(array_keys5)):
        pass
        # print(array_keys5[i])

    array_values= to_python.values()
    array_values1= str(array_values)
    array_values2= array_values1.replace("([","")
    array_values3=array_values2.replace("])","")
    array_values4=array_values3.replace("dict_values","")
    array_values5=array_values4.replace("'","")
    # array_values5=array_values5.replace("'","")
    array_values5= array_values5.split(",")
    
    print(array_values5)
      
    # print(array_keys)
    # print(array_keys4)
    # print(time_start)
    # print(time_end)
    # print(time_calc)