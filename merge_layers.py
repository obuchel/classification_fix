<<<<<<< HEAD
import json
data0={}
with open("../ARG_adm4.json", "r") as read_file:
=======

import json
data0={}
with open("ARG_adm2.json", "r") as read_file:
>>>>>>> 78c18e17230951576ec3775f38adc6fd2dd422b8
    data=json.load(read_file)
    data0=data
#'properties': {'ID_0': 12, 'ISO': 'ARG', 'NAME_0': 'Argentina', 'ID_1': 24, 'NAME_1': 'Tucumán', 'ID_2': 502, 'NAME_2': 'Trancas', 'TYPE_2': 'Departamento', 'ENGTYPE_2': 'Department', 'NL_NAME_2': '', 'VARNAME_2': ''}

<<<<<<< HEAD
with open("communas.json", "r") as read_file:
=======
with open("converter3.geojson", "r") as read_file:
>>>>>>> 78c18e17230951576ec3775f38adc6fd2dd422b8
    data2=json.load(read_file)
    for el in data2["features"]:
        #{'BARRIOS': 'BELGRANO - COLEGIALES - NUÑEZ', 'PERIMETRO': 26198.8269533, 'AREA': 14713213.1821, 'COMUNAS': 13.0, 'ID': 15, 'OBJETO': 'LIMITE COMUNAL'}
        #print(el["properties"])
        el["properties"]["NAME_1"]="Ciudad de Buenos Aires"
        el["properties"]["NAME_2"]="COMUNA "+str(el["properties"]['COMUNAS']).split(".")[0]
        el["properties"]["ID_2"]="com_"+str(el["properties"]["ID"])
        print(el)
        data0["features"].append(el)
#print(data0)

with open("ARG_adm3.json", "w") as read_file:
    json.dump(data0,read_file)
