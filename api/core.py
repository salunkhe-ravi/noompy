from traceback import print_stack
import pandas as pd
import json


def _query_builder(data_frame, query):
    """
    It builds a new dataframe depending on the where clause.
    :param data_frame: The dataframe created by reading the csv file
    :param query: Query given by the user.
    :return: Dataframe created by the where clause, else an empty dataframe.
    """
    if "WHERE" in query:
        query_str = query.split("WHERE")[1].strip()
        return data_frame.query(query_str.replace("=", "==").replace(" AND ", " and ").replace(" OR ", " or "))
    else:
        return pd.DataFrame()


def execute_query(global_excel_file_path, query, index_of_record):
    """
    This function executes the query given by the User
    :param global_excel_file_path: Path to the file to read
    :param query: Query given by the user
    :param index_of_record: The index of data which is to be selected or updated. Default index is 0.
    :return: True if update is successful
    """
    if query.startswith("SELECT"):
        # extracting sheet name
        sheet_name = query.split("FROM")[1].split("WHERE")[0].strip()
        # getting the sheet in memory and making a dataframe
        data = pd.read_excel(global_excel_file_path, sheet_name=sheet_name)

        # resolving query to a dataframe string
        query_string = _query_builder(data, query)
        if query_string.empty:
            return "WHERE clause did not retrieve any matching result."

        # For time being only take the first record
        res = query_string.to_dict(orient='records')[index_of_record]

        # To get the list of columns whose data is required.
        select_arg_list = query.split("FROM")[0].strip().split(",")
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

    elif query.startswith("UPDATE"):
        # extracting sheet name
        sheet_name = query.split("SET")[0].split(" ")[1].strip()
        # getting the sheet in memory and making a dataframe
        data = pd.read_excel(global_excel_file_path, sheet_name=sheet_name)

        # resolving query to a dataframe string
        res_df = _query_builder(data, query)
        if res_df.empty:
            return "Where Clause did not retrieve any matching result."

        # To get the list of columns whose data is to be updated
        select_arg_list = query.split("WHERE")[0].split("SET")[1].strip().split(",")
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
        data.update(res_df)
        data.to_excel(global_excel_file_path, index=False)
        return True
    else:
        print("Please provide valid query expression. Only SELECT and UPDATE statements are supported.")
        print_stack()
