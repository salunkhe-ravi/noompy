import pandas as pd


def where_clause(data_frame, query):
    if "WHERE" in query:
        query_str = query.split("WHERE")[1].strip()
        return data_frame.query(query_str.replace("=", "==").replace(" AND ", " and ").replace(" OR ", " or "))
    else:
        return pd.DataFrame()


def check_data_source(data_frame):
    if data_frame.empty:
        return True
