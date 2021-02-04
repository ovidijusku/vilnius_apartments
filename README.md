# Vilnius apartments data

This project is based on Python 3.8. It consist of [scrapping function](https://github.com/ovidijusku/vilnius_apartments/blob/main/apartments/apartments.py) which can be used to web scrape https://www.aruodas.lt and extract the dataset of apartments in Vilnius.

### Dependencies
* Python >= 3.6;
* pandas;
* requests;
* pytest (for testing only).

### Installation

> pip install git+https://github.com/ovidijusku/vilnius_apartments.git

### Access

> from apartments import apartments

### Function in use

> apartments_df = apartments.scrapper(apartments_count)

Apartments count should be inserted as an integer which shows how long should be the dataset.

Function returns pandas dataframe.

### Dataframe columns

> .add(a,b) - returns sum of a and b

> .substract(a,b) - returns b substracted from a

> .multiply(a,b) - returns product of a and b

> .divide(a,b) - returns division a from b

> .n_root(a,n) - returns n root of a

> .previous_result() - returns previous result

> .memory_reset() - resets memory

### License

Copyright protected by [MIT](https://github.com/ovidijusku/calc/blob/main/LICENSE).
