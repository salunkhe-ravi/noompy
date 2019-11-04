# from api.noompy import NoomPy
#
#
# # "SELECT wheel_base FROM Sheet1 WHERE make=bmw AND curb_weight=2395 AND body_style=sedan"
# # "SELECT * FROM Sheet1 WHERE tc_id=19"
# # SELECT wheel_base FROM Sheet1 WHERE make=bmw AND curb_weight=2395
#
# # "UPDATE Sheet1 SET wheel_base=45.66 WHERE tc_id=4.jgf"
#
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
#
# # noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=4.jgf")
#
# res = noom.select_data(select_query="INSERT INTO Sheet1(Name,Country) VALUES(Peter,UK)")
#
# # print(noom.get_data(data=res, key='tc_id'))
# print(res)
#
# x = '4.jgf'
# print(x.upper().isupper())



# "Select * from Sheet1 where make='audi'" -- will return a dataframe will filtered results based on the query
# "Select * from Sheet1 where make='audi' and body_style='ravi'"
# "Select length from Sheet1 where make='audi'"
# "Select wheel_base from Sheet1 where make='audi' and body_style='ravi'"

# "Update Sheet1 Set Country='US' where ID=100 and name='John'";
# "Select * from Sheet1 where make='audi' and body_style='ravi'"
# "Select * from Sheet1 where make='audi'"
# "Select length from Sheet1 where make='audi'"
# "Select wheel_base, length from Sheet1 where make='audi' and body_style='ravi'"
# "Select wheel_base, length from Sheet1"

# "Update Sheet1 Set Country='US' where ID=100 and name=John";




#

# query = "UPDATE Sheet1 SET Country='US' WHERE ID=100 and name=John";
#
# print(query.split("WHERE")[0].split("SET")[1].split("=")[0].strip())




# f = "ahdhd66"
#
# print(type(f) == float)


# r = "this is a test"
#
# query = "SELECT length FROM Sheet1 WHERE make='audi'"

# query = "SELECT length, fuel_type FROM Sheet1 WHERE make='audi'"
#
# print(query.split("FROM")[0].split(" ")[1])
# print(query.split("from")[0].split(" ")[1])
#
#

#
# query = "SELECT wheel_base FROM Sheet1 WHERE make=audi AND body_style=ravi"
# and_list = query.split("WHERE")[1].split("AND")
# and_list = str(and_list)
#
# print(and_list.split("="))

# print()

# print(type(10)==str)

import pandas as pd
import json
data = pd.read_excel("../sample_datasheet.xlsx", sheet_name='Sheet1')
data.loc[(data['tc_id'] == '4.jgf') & (data['num_of_doors'] == 'ravi'), 'wheel_base'] = "testvaluenew"
print(data)
print(data.to_excel("../sample_datasheet.xlsx", index=False))


    # get('fuel_type').to_string(index=False)
# res = data[data['make'] == 'audi']
# res = res.replace("[", "").replace("]", "").replace("{","").replace("}","")
# res = res.replace("\"","'").replace("'","")
# res_split = res.split(",")
#
# result_dict = {}
#
# for i in res_split:
#     ind_split = i.split(":")
#     result_dict[ind_split[0]] = ind_split[1]
#
# print(res)
# print(result_dict)
# print(type(res))
# print(type(result_dict))
# print(result_dict.get('tc_id'))



# print(r.split(" ", 1)[0].upper())
#
# s = "saturn"
# print(s[::-1])
