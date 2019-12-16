import pandas as pd
from traceback import print_stack
import json
import utils


class SelectOperation:
    def __init__(self, file_path, query):
        self.query = query
        # extracting sheet name
        self.sheet_name = query.split("FROM")[1].split("WHERE")[0].strip()
        # getting the sheet in memory and making a dataframe
        self.data = pd.read_excel(file_path, sheet_name=self.sheet_name)

    def operate(self, index_of_record=0):
        """
        :param index_of_record: This indicates the index of record user wants to delete in case of multiple records.
        Default is 0.
        :return: JSON response of the data frame else EMPTY_DF string in case of no data matches with where clause.
        """
        if utils.check_data_source(self.data):
            return json.dumps("Data source is EMPTY, Invalid Action.")
        # resolving query to a dataframe string
        query_string = utils.where_clause(self.data, self.query)
        if query_string.empty:
            return json.dumps("WHERE clause did not retrieve any matching result.")

        # For time being only take the first record
        res = query_string.to_dict(orient='records')[index_of_record]

        # To get the list of columns whose data is required.
        select_arg_list = self.query.split("FROM")[0].split("SELECT")[1].strip().split(",")

        if len(select_arg_list) == 1 and "*" in select_arg_list:
            return json.dumps(res)
        else:
            result_dict = {}
            for key in select_arg_list:
                result_dict[key.strip()] = res.get(key.strip())
            return json.dumps(result_dict)


class UpdateOperation:
    def __init__(self, file_path, query):
        self.query = query
        self.file_path = file_path
        # extracting sheet name
        self.sheet_name = query.split("SET")[0].split(" ")[1].strip()
        # getting the sheet in memory and making a dataframe
        self.data = pd.read_excel(file_path, sheet_name=self.sheet_name)

    def operate(self, index_of_record=0, auto_save=True):
        """
        :param index_of_record: This indicates the index of record user wants to delete in case of multiple records.
        Default is 0.
        :param auto_save: This when set to True will save the dataframe to the excel file and return True,
        else it will delete the row/cell/column depending on query and return the modified data frame.
        :return: True if auto save is set, else it will return the modified data frame.
        """
        if utils.check_data_source(self.data):
            return json.dumps("Data source is EMPTY, Invalid Action.")
        # resolving query to a dataframe string
        res_df = utils.where_clause(self.data, self.query)
        if res_df.empty:
            return json.dumps("WHERE clause did not retrieve any matching result.")

        # To get the list of columns whose data is to be updated
        select_arg_list = self.query.split("WHERE")[0].split("SET")[1].strip().split(",")
        col_name = []
        new_col_val = []
        for val in select_arg_list:
            k, v = val.split("=")
            col_name.append(k.strip())
            new_col_val.append(v.strip().strip("'"))

        # Updating the column values. The copy prevents SettingWithCopyWarning warning.
        res_df = res_df.loc[[res_df.index.values[index_of_record]], col_name].copy()
        res_df.loc[[res_df.index.values[index_of_record]], col_name] = new_col_val

        # Updating main dataframe.
        self.data.update(res_df)

        if auto_save:
            self.data.to_excel(self.file_path, index=False)
            return True
        return self.data


class DeleteOperation:
    def __init__(self, file_path, query):
        self.query = query
        self.file_path = file_path
        # extracting sheet name
        self.sheet_name = query.split("FROM")[1].split("WHERE")[0].strip()
        # getting the sheet in memory and making a dataframe
        self.data = pd.read_excel(file_path, sheet_name=self.sheet_name)

    def operate(self, index_of_record=0, auto_save=True):
        """
        :param index_of_record: This indicates the index of record user wants to delete in case of multiple records.
        Default is 0.
        :param auto_save: This when set to True will save the dataframe to the excel file and return True,
        else it will delete the row/cell/column depending on query and return the modified data frame.
        :return True if auto save is set, else it will return the modified data frame.
        """
        # Check if the data read from source is not empty
        if utils.check_data_source(self.data):
            return json.dumps("Data source is EMPTY, Invalid Action.")

        # Check if the operation is for deleting a row/column/cell
        query_lst = self.query.split()
        if "DELETEROW" in query_lst[0]:
            self.data = self._delete_row(index_of_record)
        elif "DELETECELL" in query_lst[0]:
            self._delete_cell(index_of_record)
        elif "DELETECOLUMN" in query_lst[0]:
            self.data = self._delete_column()

        # This will check if cell/row/column deletion returns any string data(in case of empty where clause)
        # Auto save when set will save the data to excel sheet, else it will return the data frame.
        if isinstance(self.data, str):
            return self.data
        elif auto_save:
            self.data.to_excel(self.file_path, index=False)
            return True
        return self.data

    def _delete_cell(self, index_of_record):
        res_df = utils.where_clause(self.data, self.query)
        if res_df.empty:
            return json.dumps("WHERE clause did not retrieve any matching result.")
        # To get the list of columns whose data is to be updated
        column_lst = self.query.split("FROM")[0].split("DELETECELL")[1].strip().split(",")

        # Strip any white spaces in between the elements of column_lst.
        col_lst = []
        for col in column_lst:
            col_lst.append(col.strip())

        # Updating the column values. The copy prevents SettingWithCopyWarning warning.
        res_df = res_df.loc[[res_df.index.values[index_of_record]], col_lst].copy()
        res_df.loc[[res_df.index.values[index_of_record]], col_lst] = ""

        # Updating main dataframe.
        return self.data.update(res_df)

    def _delete_row(self, index_of_record):
        res_df = utils.where_clause(self.data, self.query)
        if res_df.empty:
            return json.dumps("WHERE clause did not retrieve any matching result.")
        return self.data.drop(res_df.index.values[index_of_record])

    def _delete_column(self):
        # Filter list of columns for deletion
        column_lst = self.query.split("FROM")[0].split("DELETECOLUMN")[1].strip().split(",")

        # Strip any white spaces in between the elements of list.
        col_lst = []
        for col in column_lst:
            col_lst.append(col.strip())

        return self.data.drop(columns=col_lst, axis=1)
