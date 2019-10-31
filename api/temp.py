# r = "this is a test"
#
# query = "Select length from Sheet1 where make='audi'"

query = "Select length, fuel_type from Sheet1 where make='audi'"

print(query.split("from")[0].split(","))
# print(query.split("from")[0].split(" ")[1])





# import pandas as pd
#
# data = pd.read_excel("../sample_datasheet.xlsx", sheet_name='Sheet1')
#
# # res = data[(data['make'] == 'audi') & (data['body_style'] == 'ravi')].get('fuel_type').to_string(index=False)
#
# res = data[data['make'] == 'audi']
# print(str(res))



# print(r.split(" ", 1)[0].upper())
#
# s = "saturn"
# print(s[::-1])
