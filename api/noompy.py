from api.core import execute_query
from traceback import print_stack
from os import path

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

    def select_data(self, select_query):
        """
        selects and retrieves a single or multiple data set from given excel workbook source as provided
        :param select_query:
        :return: single or multiple data
        """
        result = execute_query(global_excel_file_path, select_query)
        return result

    def update_data(self, update_query):
        """
        updates the given column value provided in the query with where condition
        :param update_query:
        :return: success message
        """
        result = execute_query(global_excel_file_path, update_query)
        return result

    def get_data(self, data=None, key=None):
        """
        gets you the needed column value(key) from the provided data
        :param data: data retrieved from noom.select_data()
        :param key: column name
        :return: value for the provided key(column)
        """
        if data and key is not None:
            return data.get(key)
        else:
            print('data or key is None')
