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

apartments_count should be inserted as an integer which shows how long should be the dataset.

Function returns pandas dataframe.

### Dataframe columns

* num_rooms - number of rooms in apartment
* area - area in sq. meters of apartment
* years_built - years when the object was built
* heating - heating system in the apartment
* completeness - level of completeness of the apartment
* district - specific Vilnius district where the object is
* price - wanted price by the owner in EUR

### Testing

![](https://raw.githubusercontent.com/ovidijusku/vilnius_apartments/main/test/test.bmp)

### License

Copyright protected by [MIT](https://github.com/ovidijusku/calc/blob/main/LICENSE).
