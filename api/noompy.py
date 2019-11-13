from api.core import execute_query
from traceback import print_stack
from os import path
import json

__author__ = "Ravi Salunkhe"
__modified_by__ = "Akshay Deshpande"


class NoomPy:
    def __init__(self, excel_path=None):
        if excel_path is not None:
            if path.exists(excel_path):
                self.global_excel_file_path = excel_path
            else:
                print("excel_path provided does not exist, please check")
                print_stack()
        else:
            print('Please provide the excel_path')
            print_stack()

    def select_data(self, select_query, index_of_record=0):
        """
        selects and retrieves a single or multiple data set from given excel workbook source as provided
        :param index_of_record: This indicates index of record user wants in case of multiple records. Default is 0
        :param select_query: Query given by user
        :return: single data and/or number of query matches
        """
        return execute_query(self.global_excel_file_path, select_query, index_of_record)

    def update_data(self, update_query, index_of_record=0):
        """
        updates the given column value provided in the query with where condition
        :param index_of_record: This indicates index of record user wants in case of multiple records. Default is 0
        :param update_query: Query given by User
        :return: success message
        """
        return execute_query(self.global_excel_file_path, update_query, index_of_record)

    @staticmethod
    def get_data(data=None, key=None):
        """
        gets you the needed column value(key) from the provided data
        :param data: data retrieved from noom.select_data(), Data Type - JSON
        :param key: column name
        :return: value for the provided key(column)
        """
        data = json.loads(data)
        if data and key is not None:
            return data.get(key)
        else:
            print('data or key is None')
