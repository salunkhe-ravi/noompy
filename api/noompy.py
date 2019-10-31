import pandas as pd
from api.core import resolve_query, execute_query
from traceback import print_stack
from os import path

query = "Select * from Sheet1 where make='audi' and body_style='ravi'"

# "Select * from Sheet1 where make='audi' and body_style='ravi'"
# "Select * from Sheet1 where make='audi'"
# "Select length from Sheet1 where make='audi'"
# "Select wheel_base, length from Sheet1 where make='audi' and body_style='ravi'"
# "Select wheel_base, length from Sheet1"


__author__ = "Ravi Salunkhe"


class NoomPy:
    global_excel_file_path = None

    def __init__(self, excel_path=None):
        global global_excel_file_path
        if excel_path is not None:
            if path.exists(excel_path):
                global_excel_file_path = excel_path
            else:
                print("excel_path provided does not exist, please check")
                print_stack()
        else:
            print('Please provide the excel_path')
            print_stack()

    def get_data(self, select_query):
        result = execute_query(global_excel_file_path, select_query)
        return result

    def insert_data(self, insert_query):
        pass

    def update_data(self, update_query):
        pass

    # data = pd.read_excel("sample_datasheet.xlsx", sheet_name='Sheet1')
    #
    # res = data[(data['make'] == 'audi') & (data['body_style'] == 'ravi')].get('fuel_type').to_string(index=False)
    #
    # print(str(res))
