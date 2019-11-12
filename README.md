
[![PyPI download month](https://img.shields.io/pypi/dm/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)  [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

# noompy
noompy is an Excel API which helps you to "query" your .xls & .xlsx files. It supports SELECT and UPDATE statements.

## Getting Started

### Pre-requisites

```
python version >= 3.6
```

### Installing

```
pip install noompy
```

## Usage

### Note: 

* Use SELECT, INSERT, WHERE and AND clauses in CAPITAL while writing the query.
* A maximum of 4 "AND" conditions could be added to the query statement 

### SELECT Query Examples

#### Example # 1

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name=some_col_value")
get_col_value = noom.get_data(data=res, key='some_key_col_name')
print(get_col_value)
print(res)

```

#### Example # 2

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT col_name FROM sheet_name WHERE col_name=some_col_value")
print(res)

```

#### Example # 3

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name1=some_col_value1 AND col_name2=some_col_value2")
get_col_value = noom.get_data(data=res, key='some_key_col_name')
print(get_col_value)
print(res)

```

#### Example # 4

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name1=some_col_value1 AND col_name2=some_col_value2 AND col_name3=some_col_value3")
get_col_value = noom.get_data(data=res, key='some_key_col_name')
print(get_col_value)
print(res)

```


#### Example # 5

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name1=some_col_value1 AND col_name2=some_col_value2 AND col_name3=some_col_value3 AND col_name4=some_col_value4")
get_col_value = noom.get_data(data=res, key='some_key_col_name')
print(get_col_value)
print(res)

```


#### Example # 6

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name1=some_col_value1 AND col_name2=some_col_value2 AND col_name3=some_col_value3 AND col_name4=some_col_value4 AND col_name5=some_col_value5")
get_col_value = noom.get_data(data=res, key='some_key_col_name')
print(get_col_value)
print(res)

```

### UPDATE Query Examples

#### Example # 1

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.update_data(update_query="UPDATE sheet_name SET col_name=col_value WHERE col_name=some_col_value")
print(res)

```

#### Example # 2

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.update_data(update_query="UPDATE sheet_name SET col_name=col_value WHERE col_name1=some_col_value1 AND col_name2=some_col_value2")
print(res)

```

## Built With

* [pandas](https://pandas.pydata.org/pandas-docs/stable/) - The core framework used for excel dataframe manipulation
* [openpyxl/xlrd/xlwt](http://www.python-excel.org/) - For working with Excel read/write etc.


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

Used [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/salunkhe-ravi/noompy/tags). 

## Authors

* **Ravi Salunkhe** - *Initial work* - [salunkhe-ravi](https://github.com/salunkhe-ravi)

See also the list of [contributors](https://github.com/salunkhe-ravi/noompy/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

* Inspired by [fillo](https://codoid.com/fillo/) - Java based Excel API

