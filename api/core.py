import pandas as pd
from traceback import print_stack
import json


class CommonOperations:
    @staticmethod
    def where_clause(data_frame, query):
        if "WHERE" in query:
            query_str = query.split("WHERE")[1].strip()
            return data_frame.query(query_str.replace("=", "==").replace(" AND ", " and ").replace(" OR ", " or "))
        else:
            return pd.DataFrame()


class SelectOperation(CommonOperations):
    def __init__(self, file_path, query):
        self.query = query
        # extracting sheet name
        self.sheet_name = query.split("FROM")[1].split("WHERE")[0].strip()
        # getting the sheet in memory and making a dataframe
        self.data = pd.read_excel(file_path, sheet_name=self.sheet_name)

    def operate(self, index_of_record=0):
        # resolving query to a dataframe string
        query_string = self.where_clause(self.data, self.query)
        if query_string.empty:
            return "WHERE clause did not retrieve any matching result."

        # For time being only take the first record
        res = query_string.to_dict(orient='records')[index_of_record]

        # To get the list of columns whose data is required.
        select_arg_list = self.query.split("FROM")[0].strip().split(",")
        # To remove SELECT keyword.
        temp = select_arg_list[0].strip("SELECT")
        select_arg_list.pop(0)
        select_arg_list.insert(0, temp.strip())

        if len(select_arg_list) == 1 and "*" in select_arg_list:
            return json.dumps(res)
        else:
            result_dict = {}
            for key in select_arg_list:
                result_dict[key.strip()] = res.get(key.strip())
            return json.dumps(result_dict)


class UpdateOperation(CommonOperations):
    def __init__(self, file_path, query):
        self.query = query
        self.file_path = file_path
        # extracting sheet name
        self.sheet_name = query.split("SET")[0].split(" ")[1].strip()
        # getting the sheet in memory and making a dataframe
        self.data = pd.read_excel(file_path, sheet_name=self.sheet_name)

    def operate(self, index_of_record=0, auto_save=True):
        # resolving query to a dataframe string
        res_df = self.where_clause(self.data, self.query)
        if res_df.empty:
            return "Where Clause did not retrieve any matching result."

        # To get the list of columns whose data is to be updated
        select_arg_list = self.query.split("WHERE")[0].split("SET")[1].strip().split(",")
        col_name = []
        new_col_val = []
        for val in select_arg_list:
            k, v = val.split("=")
            col_name.append(k.strip())
            new_col_val.append(v.strip().strip("'"))

        # Updating the column values. The copy prevents SettingWithCopyWarning warning.
        res_df = res_df.loc[[list(res_df.index.values)[index_of_record]], col_name].copy()
        res_df.loc[[list(res_df.index.values)[index_of_record]], col_name] = new_col_val

        # Updating main dataframe.
        self.data.update(res_df)

        if auto_save:
            self.data.to_excel(self.file_path, index=False)
            return True
        return self.data


class DeleteOperation(CommonOperations):
    def __init__(self, file_path, query):
        self.query = query
        self.file_path = file_path
        # extracting sheet name
        self.sheet_name = query.split("FROM")[1].split("WHERE")[0].strip()
        # getting the sheet in memory and making a dataframe
        self.data = pd.read_excel(file_path, sheet_name=self.sheet_name)

    def operate(self, index_of_record=0):
        res_df = self.where_clause(self.data, self.query)
        if res_df.empty:
            return "Where Clause did not retrieve any matching result."
        self.data = self.data.drop(res_df.index.values[index_of_record])
        self.data.to_excel(self.file_path, index=False)
        return True

