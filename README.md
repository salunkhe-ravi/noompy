
[![Downloads](https://pepy.tech/badge/noompy)](https://pepy.tech/project/noompy)  [![Downloads](https://pepy.tech/badge/noompy/month)](https://pepy.tech/project/noompy/month)  [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.org/project/noompy/)

# noompy
noompy is a simple minimalistic Excel API which helps you to "query" your .xls & .xlsx files. It supports SELECT and UPDATE statements as well as WHERE, AND and OR conditions.

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

* Use SELECT, UPDATE, WHERE, OR and AND clauses in CAPITAL while defining your query.

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
res = noom.select_data(select_query="SELECT col_name1 FROM sheet_name WHERE col_name=some_col_value")
print(res)

```

#### Example # 3

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT col_name1, col_name2, col_name3 FROM sheet_name WHERE col_name=some_col_value")
print(res)

```

#### Example # 4

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name1=some_col_value1 AND col_name2=some_col_value2")
get_col_value = noom.get_data(data=res, key='some_key_col_name')
print(get_col_value)
print(res)

```

#### Example # 5

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name1=some_col_value1 AND col_name2=some_col_value2 OR col_name3=some_col_value3")
get_col_value = noom.get_data(data=res, key='some_key_col_name')
print(get_col_value)
print(res)

```


#### Example # 6

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name1=some_col_value1 AND col_name2=some_col_value2 AND col_name3=some_col_value3 AND col_name4=some_col_value4")
get_col_value = noom.get_data(data=res, key='some_key_col_name')
print(get_col_value)
print(res)

```


#### Example # 7

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.select_data(select_query="SELECT * FROM sheet_name WHERE col_name1=some_col_value1 OR col_name2=some_col_value2 AND col_name3=some_col_value3 AND col_name4=some_col_value4 AND col_name5=some_col_value5")
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
res = noom.update_data(update_query="UPDATE sheet_name SET col_name=col_value WHERE col_name1=some_col_value1 OR col_name2=some_col_value2")
print(res)

```

#### Example # 3

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='path_to_.xlsx')
res = noom.update_data(update_query="UPDATE sheet_name SET col_name1=col_value1, col_name2=col_value2 WHERE col_name1=some_col_value1 AND col_name2=some_col_value2")
print(res)

```

## Built With

* [pandas](https://pandas.pydata.org/pandas-docs/stable/) - The core package used for excel dataframe manipulation
* [openpyxl/xlrd/xlwt](http://www.python-excel.org/) - For working with Excel read/write etc.


# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [Unreleased]
- Support for LIKE clause in query
- Feature to support Excel cell formatting

## [1.10] - 2019-11-13

### Added
- Support for single/multiple 'OR' clause in the SELECT/UPDATE queries and a combination of AND/OR will also work.
- We can now use multiple column names in SELECT/UPDATE statements separated by comma(,) for data retrieval
- index_of_record argument in SELECT/UPDATE functions which indicates the index of record user wants in case of multiple records. Default is 0

### Changed
- query_builder function and its implementation to work with multiple combinations of AND/OR clause statements 
- The logic to parse the SELECT/UPDATE query statements to handle n-number of AND conditions.
- get_data() method to static

### Removed
- A maximum limit of 4 "AND" conditions to be added to the query statement
- Support for single column in SELECT/UPDATE statements for data retrieval  


## [1.0.1] - 2019-11-04
- Initial Release


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

