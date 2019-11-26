import core
from traceback import print_stack
from os import path
import json

__author__ = "Ravi Salunkhe"
__modified_by__ = "Akshay Deshpande"


class NoomPy:
    def __init__(self, excel_path=None):
        if excel_path is not None:
            if path.exists(excel_path):
                self.excel_file_path = excel_path
            else:
                print("excel_path provided does not exist, please check")
                print_stack()
        else:
            print('Please provide the excel_path')
            print_stack()

    def select_data(self, select_query, index_of_record=0):
        """
        Selects and retrieves a single or multiple data set from given excel workbook source as provided.
        :param index_of_record: This indicates index of record user wants in case of multiple records. Default is 0.
        :param select_query: Query given by user.
        :return: Single data and/or number of query matches.
        """
        return core.SelectOperation(self.excel_file_path, select_query).operate(index_of_record)

    def update_data(self, update_query, index_of_record=0, auto_save=True):
        """
        Updates the given column value provided in the query with where condition.
        :param index_of_record: This indicates index of record user wants in case of multiple records. Default is 0.
        :param update_query: Query given by User.
        :param auto_save: This when set to True will save the updated data in the excel file and return True,
        else it will not dump the data to excel file and will return the DataFrame. Default is True.
        :return: True if auto_save is set, else it will return the data frame.
        """
        return core.UpdateOperation(self.excel_file_path, update_query).operate(index_of_record, auto_save)

    def delete_data(self, delete_query, index_of_record=0):
        """
        Deletes the given row provided in the query with where condition.
        :param delete_query: Query given by user.
        :param index_of_record: This indicates the index of record user wants to delete in case of multiple records.
                                Default is 0.
        :return: Success message.
        """
        return core.DeleteOperation(self.excel_file_path, delete_query).operate(index_of_record)

    @staticmethod
    def get_data(data=None, key=None):
        """
        Gets you the needed column value(key) from the provided data.
        :param data: Data retrieved from noom.select_data(), Data Type - JSON.
        :param key: Column name.
        :return: Value for the provided key(column).
        """
        data = json.loads(data)
        if data and key is not None:
            return data.get(key)
        else:
            print('data or key is None')
