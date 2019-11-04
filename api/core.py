from traceback import print_stack
import pandas as pd

data = None
query_type = None

def query_builder(data, query):
    # splitting the query to work on building the expression from the "from" part
    # only supported till 4 "AND" statements
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
                elif "." in mod2 and not mod2.upper().isupper():
                    mod2 = float(mod2)
                mod3 = expression[2].strip()
                mod4 = expression[3].strip()
                if mod4.isdigit():
                    mod4 = int(mod4)
                elif "." in mod4 and not mod4.upper().isupper():
                    mod4 = float(mod4)
                if query.startswith("SELECT"):
                    exp = data[(data[mod1] == mod2) & (data[mod3] == mod4)]
                elif query.startswith("UPDATE"):
                    col_name = query.split("WHERE")[0].split("SET")[1].split("=")[0].strip()
                    col_value = query.split("WHERE")[0].split("SET")[1].split("=")[1].strip()
                    data.loc[(data[mod1] == mod2) & (data[mod3] == mod4), col_name] = col_value
                    return "pass"

                return exp
            elif and_count == 2:
                expression = [x for a in temp_list for x in a.strip().split("=")]

                mod1 = expression[0].strip()
                mod2 = expression[1].strip()
                if mod2.isdigit():
                    mod2 = int(mod2)
                elif "." in mod2 and not mod2.upper().isupper():
                    mod2 = float(mod2)
                mod3 = expression[2].strip()
                mod4 = expression[3].strip()
                if mod4.isdigit():
                    mod4 = int(mod4)
                elif "." in mod4 and not mod4.upper().isupper():
                    mod4 = float(mod4)
                mod5 = expression[4].strip()
                mod6 = expression[5].strip()
                if mod6.isdigit():
                    mod6 = int(mod6)
                elif "." in mod6 and not mod6.upper().isupper():
                    mod6 = float(mod6)

                if query.startswith("SELECT"):
                    exp = data[(data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6)]
                elif query.startswith("UPDATE"):
                    col_name = query.split("WHERE")[0].split("SET")[1].split("=")[0].strip()
                    exp = data.loc[(data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6), col_name]

                return exp

            elif and_count == 3:
                expression = [x for a in temp_list for x in a.strip().split("=")]

                mod1 = expression[0].strip()
                mod2 = expression[1].strip()
                if mod2.isdigit():
                    mod2 = int(mod2)
                elif "." in mod2 and not mod2.upper().isupper():
                    mod2 = float(mod2)
                mod3 = expression[2].strip()
                mod4 = expression[3].strip()
                if mod4.isdigit():
                    mod4 = int(mod4)
                elif "." in mod4 and not mod4.upper().isupper():
                    mod4 = float(mod4)
                mod5 = expression[4].strip()
                mod6 = expression[5].strip()
                if mod6.isdigit():
                    mod6 = int(mod6)
                elif "." in mod6 and not mod6.upper().isupper():
                    mod6 = float(mod6)
                mod7 = expression[6].strip()
                mod8 = expression[7].strip()
                if mod8.isdigit():
                    mod8 = int(mod8)
                elif "." in mod8 and not mod8.upper().isupper():
                    mod8 = float(mod8)

                if query.startswith("SELECT"):
                    exp = data[
                        (data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6) & (data[mod7] == mod8)]
                elif query.startswith("UPDATE"):
                    col_name = query.split("WHERE")[0].split("SET")[1].split("=")[0].strip()
                    exp = data.loc[(data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6) & (
                            data[mod7] == mod8), col_name]

                return exp

            elif and_count == 4:
                expression = [x for a in temp_list for x in a.strip().split("=")]

                mod1 = expression[0].strip()
                mod2 = expression[1].strip()
                if mod2.isdigit():
                    mod2 = int(mod2)
                elif "." in mod2 and not mod2.upper().isupper():
                    mod2 = float(mod2)
                mod3 = expression[2].strip()
                mod4 = expression[3].strip()
                if mod4.isdigit():
                    mod4 = int(mod4)
                elif "." in mod4 and not mod4.upper().isupper():
                    mod4 = float(mod4)
                mod5 = expression[4].strip()
                mod6 = expression[5].strip()
                if mod6.isdigit():
                    mod6 = int(mod6)
                elif "." in mod6 and not mod6.upper().isupper():
                    mod6 = float(mod6)
                mod7 = expression[6].strip()
                mod8 = expression[7].strip()
                if mod8.isdigit():
                    mod8 = int(mod8)
                elif "." in mod8 and not mod8.upper().isupper():
                    mod8 = float(mod8)
                mod9 = expression[8].strip()
                mod10 = expression[9].strip()
                if mod10.isdigit():
                    mod10 = int(mod10)
                elif "." in mod10 and not mod10.upper().isupper():
                    mod10 = float(mod10)

                if query.startswith("SELECT"):
                    exp = data[
                        (data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6) & (data[mod7] == mod8) & (
                                data[mod9] == mod10)]
                elif query.startswith("UPDATE"):
                    col_name = query.split("WHERE")[0].split("SET")[1].split("=")[0].strip()
                    exp = data.loc[(data[mod1] == mod2) & (data[mod3] == mod4) & (data[mod5] == mod6) & (
                            data[mod7] == mod8) & (
                                           data[mod9] == mod10), col_name]

                return exp
        else:
            # else if there's none
            expression = query.split("WHERE")[1].split("=")
            # checking whether the number is numeric, float or alphanumeric and building relevant expression
            mod1 = expression[0].strip()
            mod2 = expression[1].strip()

            if mod2.isdigit():
                mod2 = int(mod2)
            elif "." in mod2 and not mod2.upper().isupper():
                mod2 = float(mod2)

            if query.startswith("SELECT"):
                exp = data[(data[mod1] == mod2)]
            elif query.startswith("UPDATE"):
                col_name = query.split("WHERE")[0].split("SET")[1].split("=")[0].strip()
                col_value = query.split("WHERE")[0].split("SET")[1].split("=")[1].strip()
                data.loc[(data[mod1] == mod2), col_name] = col_value
                return "pass"
            return exp


def execute_query(global_excel_file_path, query):
    # logic if the query starts with select
    if query.startswith("SELECT"):
        # extracting sheet name
        sheet_name = query.split("FROM")[1].split("WHERE")[0].strip()
        # getting the sheet in memory and making a dataframe
        data = pd.read_excel(global_excel_file_path, sheet_name=sheet_name)
        # resolving query to a dataframe string
        query_string = query_builder(data, query)
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

    elif query.startswith("UPDATE"):
        # extracting sheet name
        sheet_name = query.split("SET")[0].split(" ")[1].strip()
        # getting the sheet in memory and making a dataframe
        data = pd.read_excel(global_excel_file_path, sheet_name=sheet_name)
        # resolving query to a dataframe string
        query_string = query_builder(data, query)
        if query_string:
            data.to_excel(global_excel_file_path, index=False)
            return "UPDATE Successfull!"
        else:
            print("Error while performing UPDATE")
            print_stack()
    else:
        print("Please provide valid query expression. Only SELECT and UPDATE statements are supported.")
        print_stack()
