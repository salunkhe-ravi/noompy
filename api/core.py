from traceback import print_stack
import pandas as pd

data = None


def resolve_query(data, query):
    if query.split(" ", 1)[0].strip() == 'SELECT':
        return select_query_builder(data, query)
    elif query.split(" ", 1)[0].strip() == 'INSERT':
        pass
    elif query.split(" ", 1)[0].strip() == 'UPDATE':
        pass
    else:
        print('The query statement provided is incorrect - only SELECT, INSERT and UPDATE is supported! ')
        print_stack()


# "Select * from Sheet1 where make='audi'" -- will return a dataframe will filtered results based on the query
# "Select * from Sheet1 where make='audi' and body_style='ravi'"
# "Select length from Sheet1 where make='audi'"
# "Select wheel_base,length from Sheet1 where make='audi' and body_style='ravi'"

def select_query_builder(data, query):
    query_split = query.split(" ")
    if "WHERE" or "AND" in query:
        and_count = query.count("AND")
        if and_count >= 2:
            for a in range(and_count):
                pass
        else:
            expression = query.split("WHERE")[1].split("=")
            # int(expression[1].strip())
            if "." in expression[1].strip():
                temp = expression[1].strip().replace(".", "0")
                if temp.isdigit():
                    return data[(data[expression[0].strip()] == float(expression[1].strip()))]
                else:
                    return data[(data[expression[0].strip()] == expression[1].strip())]
            elif expression[1].strip().isdigit():
                return data[(data[expression[0].strip()] == int(expression[1].strip()))]
            else:
                return data[(data[expression[0].strip()] == expression[1].strip())]

    # data[(data['make'] == 'audi') & (data['body_style'] == 'ravi')]


def insert_query_builder():
    pass


def update_query_builder():
    pass


def execute_query(global_excel_file_path, query):
    # query = query.upper()
    if query.startswith("SELECT"):
        sheet_name = query.split("FROM")[1].split("WHERE")[0].strip()
        data = pd.read_excel(global_excel_file_path, sheet_name=sheet_name)
        query_string = resolve_query(data, query)
        if "," not in query:
            # get selectors
            select_arg_list = query.split("FROM")[0].split(" ")[1].strip()
            if select_arg_list == "*":
                return query_string.to_json()
            else:
                pass
