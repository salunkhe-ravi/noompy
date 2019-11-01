from api.noompy import NoomPy


# "SELECT wheel_base FROM Sheet1 WHERE make=bmw AND curb_weight=2395 AND body_style=sedan"
# "SELECT * FROM Sheet1 WHERE tc_id=19"
# SELECT wheel_base FROM Sheet1 WHERE make=bmw AND curb_weight=2395

noom = NoomPy(excel_path='../sample_datasheet.xlsx')

# noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=4.jgf")

res = noom.select_data(select_query="SELECT wheel_base FROM Sheet1 WHERE make=bmw AND curb_weight=2395")

# print(noom.get_data(data=res, key='tc_id'))
print(res)





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

# import pandas as pd
# import json
# data = pd.read_excel("../sample_datasheet.xlsx", sheet_name='Sheet1')
#
# res = data[(data['tc_id'] == '4.jgf')].get('fuel_type')
# print(res)
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
