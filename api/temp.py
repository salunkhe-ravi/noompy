from api.noompy import NoomPy

noom = NoomPy(excel_path='../sample_datasheet.xlsx')

data = noom.get_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=4.jgf")

print(data)



# r = "this is a test"
#
# query = "Select length from Sheet1 where make='audi'"

# query = "SELECT length, fuel_type FROM Sheet1 WHERE make='audi'"
#
# print(query.split("FROM")[1].split("WHERE")[0])
# print(query.split("from")[0].split(" ")[1])
#
#

# print(type(10)==str)

# import pandas as pd
# data = pd.read_excel("../sample_datasheet.xlsx", sheet_name='Sheet1')
#
# res = data[(data['wheel_base'] == 333333.22)].to_json()
#     # get('fuel_type').to_string(index=False)
# # res = data[data['make'] == 'audi']
# print(res)



# print(r.split(" ", 1)[0].upper())
#
# s = "saturn"
# print(s[::-1])
