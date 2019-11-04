# noompy
noompy is an Excel API which helps you to "query" your xls & xlsx files. It supports SELECT and UPDATE statements.

## Getting Started


### Installing

```
pip install noompy
```

End with an example of getting some data out of the system or using it for a little demo

## Usage

###SELECT Query Examples

#### Example # 1

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=40")
get_wheel_base = noom.get_data(data=res, key='some_col_name')
print(get_wheel_base)
print(res)

```

#### Example # 2

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
res = noom.select_data(select_query="SELECT wheel_base FROM Sheet1 WHERE tc_id=5.jgf")
print(res)

```

#### Example # 3

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=5.jgf AND wheel_base=77.77")
get_make = noom.get_data(data=res, key='make')
print(get_make)
print(res)

```

#### Example # 4

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=5.jgf AND wheel_base=77.77 AND engine_location=front")
get_make = noom.get_data(data=res, key='make')
print(get_make)
print(res)

```


#### Example # 5

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=5.jgf AND wheel_base=77.77 AND engine_location=front AND length=176.6")
get_make = noom.get_data(data=res, key='make')
print(get_make)
print(res)

```

#### Example # 5

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
res = noom.select_data(select_query="SELECT * FROM Sheet1 WHERE tc_id=5.jgf AND wheel_base=77.77 AND engine_location=front AND length=176.6 AND price=17450")
get_make = noom.get_data(data=res, key='make')
print(get_make)
print(res)

```

###UPDATE Query Examples

#### Example # 1

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
res = noom.update_data(update_query="UPDATE Sheet1 SET make=test WHERE tc_id=10.11")
print(res)

```

#### Example # 2

```
from api.noompy import NoomPy
noom = NoomPy(excel_path='../sample_datasheet.xlsx')
res = noom.update_data(update_query="UPDATE Sheet1 SET make=test2 WHERE tc_id=10.11 AND body_style=ravi")
print(res)

```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [pandas](http://www.dropwizard.io/1.0.2/docs/) - The core framework used for excel dataframe manipulation
* [xlrd/xlwt](https://maven.apache.org/) - Excel read/write


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
