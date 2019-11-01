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
# "Select wheel_base from Sheet1 where make='audi' and body_style='ravi'"

def select_query_builder(data, query):
    # splitting the query to work on building the expression from the "from" part
    query_split = query.split(" ")
    if "WHERE" or "AND" in query:
        and_count = query.count("AND")
        if and_count >= 1:
            exp = None
            # if there are multiple and statements the loop and create the expression
            temp_list = query.split("WHERE")[1].split("AND")

            if and_count == 1:
                expression = [x for a in temp_list for x in a.strip().split("=")]
                mod1 = expression[0].strip()
                mod2 = expression[1].strip()
                if mod2.isdigit():
                    mod2 = int(mod2)
                mod3 = expression[2].strip()
                mod4 = expression[3].strip()
                if mod4.isdigit():
                    mod4 = int(mod4)
                exp = data[(data[mod1] == mod2) & (data[mod3] == mod4)]
                return exp
            elif and_count == 2:
                expression = [x for a in temp_list for x in a.strip().split("=")]

                mod1 = expression[0].strip()
                mod2 = expression[1].strip()
                if mod2.isdigit():
                    mod2 = int(mod2)
                mod3 = expression[2].strip()
                mod4 = expression[3].strip()
                if mod4.isdigit():
                    mod4 = int(mod4)
                mod5 = expression[4].strip()
                mod6 = expression[5].strip()
                if mod6.isdigit():
                    mod6 = int(mod6)
                exp = data[(data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6)]
                return exp

            elif and_count == 3:
                expression = [x for a in temp_list for x in a.strip().split("=")]

                mod1 = expression[0].strip()
                mod2 = expression[1].strip()
                if mod2.isdigit():
                    mod2 = int(mod2)
                mod3 = expression[2].strip()
                mod4 = expression[3].strip()
                if mod4.isdigit():
                    mod4 = int(mod4)
                mod5 = expression[4].strip()
                mod6 = expression[5].strip()
                if mod6.isdigit():
                    mod6 = int(mod6)
                mod7 = expression[6].strip()
                mod8 = expression[7].strip()
                if mod8.isdigit():
                    mod8 = int(mod8)
                exp = data[(data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6) & (data[mod7] == mod8)]
                return exp

            elif and_count == 4:
                expression = [x for a in temp_list for x in a.strip().split("=")]

                mod1 = expression[0].strip()
                mod2 = expression[1].strip()
                if mod2.isdigit():
                    mod2 = int(mod2)
                mod3 = expression[2].strip()
                mod4 = expression[3].strip()
                if mod4.isdigit():
                    mod4 = int(mod4)
                mod5 = expression[4].strip()
                mod6 = expression[5].strip()
                if mod6.isdigit():
                    mod6 = int(mod6)
                mod7 = expression[6].strip()
                mod8 = expression[7].strip()
                if mod8.isdigit():
                    mod8 = int(mod8)
                mod9 = expression[8].strip()
                mod10 = expression[9].strip()
                if mod10.isdigit():
                    mod10 = int(mod10)
                exp = data[(data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6) & (data[mod7] == mod8) & (
                            data[mod9] == mod10)]
                return exp
        else:
            # else if there's none
            expression = query.split("WHERE")[1].split("=")
            # checking whether the number is numeric, float or alphanumeric and building relevant expression
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
    # logic if the query starts with select
    if query.startswith("SELECT"):
        # extracting sheet name
        sheet_name = query.split("FROM")[1].split("WHERE")[0].strip()
        # getting the sheet in memory and making a dataframe
        data = pd.read_excel(global_excel_file_path, sheet_name=sheet_name)
        # resolving query to a dataframe string
        query_string = resolve_query(data, query)
        if "," not in query:
            # get selectors
            select_arg_list = query.split("FROM")[0].split(" ")[1].strip()
            # this is select *
            if select_arg_list == "*":
                res = query_string.to_json(orient='records')
                res = res.replace("[", "").replace("]", "").replace("{", "").replace("}", "")
                res = res.replace("\"", "'").replace("'", "")
                res_split = res.split(",")
                result_dict = {}
                for i in res_split:
                    ind_split = i.split(":")
                    result_dict[ind_split[0]] = ind_split[1]
                return result_dict
            else:
                # this is for select <single column>
                comma_count = query.count(",")
                if comma_count >= 1:
                    print("Please use SELECT * instead of multiple SELECT <column1>, <column2>...etc")
                    print_stack()
                else:
                    select_col = query.split("FROM")[0].split(" ")[1]
                    return query_string.get(select_col.strip()).to_string(index=False).strip()

        else:
            # write multiple select columns
            print("Please use SELECT * instead of multiple SELECT <column1>, <column2>...etc")
            print_stack()


def convert_to_dictionary(res):
    pass
