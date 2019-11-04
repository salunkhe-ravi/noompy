# from api.noompy import NoomPy


# SELECT Example #1
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
# res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=4.jgf")
# get_wheel_base = noom.get_data(data=res, key='wheel_base')
# print(get_wheel_base)
# print(res)

# SELECT Example #2
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
# res = noom.select_data(select_query="SELECT wheel_base FROM Sheet1 WHERE tc_id=5.jgf")
# print(res)

# SELECT Example #3
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
# res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=5.jgf AND wheel_base=77.77")
# get_make = noom.get_data(data=res, key='make')
# print(get_make)
# print(res)

# SELECT Example #4
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
# res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=5.jgf AND wheel_base=77.77 AND engine_location=front")
# get_make = noom.get_data(data=res, key='make')
# print(get_make)
# print(res)

# SELECT Example #5
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
# res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=5.jgf AND wheel_base=77.77 AND engine_location=front AND length=176.6")
# get_make = noom.get_data(data=res, key='make')
# print(get_make)
# print(res)

# SELECT Example #6
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
# res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=5.jgf AND wheel_base=77.77 AND engine_location=front AND length=176.6 AND price=17450")
# get_make = noom.get_data(data=res, key='make')
# print(get_make)
# print(res)

# ##########################################################################################################################################

# UPDATE Example #1
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
# res = noom.update_data(update_query="UPDATE Sheet1 SET make=test WHERE tc_id=10.11")
# print(res)


# UPDATE Example #2
# noom = NoomPy(excel_path='../sample_datasheet.xlsx')
# res = noom.update_data(update_query="UPDATE Sheet1 SET make=test2 WHERE tc_id=10.11 AND body_style=ravi")
# print(res)




