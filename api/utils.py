import pandas as pd


def where_clause(data_frame, query):
    if "WHERE" in query:
        query_str = query.split("WHERE")[1].strip()
        return data_frame.query(query_str.replace("=", "==").replace(" AND ", " and ").replace(" OR ", " or "))
    else:
        return pd.DataFrame()


def strip_head_trail_ws(column_lst, keyword):
    temp = column_lst[0].strip(keyword)
    column_lst.pop(0)
    column_lst.insert(0, temp.strip())
    return column_lst


def check_data_source(data_frame):
    if data_frame.empty:
        return True
