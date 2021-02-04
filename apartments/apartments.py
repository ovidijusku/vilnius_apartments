from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


def scrapper(expected_items: int) -> pd.DataFrame:
    """Function allows to scrape aruodas.lt website for apartments data in Vilnius, expected input is integer for number of how many items should be collected"""
    page_count = 1  # index which will switch pages
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "referer": "https://www.google.com/",
    }  # client version for accessing the website

    # creating empty lists for data storage
    prices_list = []
    districts_list = []
    num_rooms_list = []
    area_list = []
    built_years_list = []
    heating_list = []
    completeness_list = []

    while len(prices_list) < expected_items:
        URL = (
            "https://m.en.aruodas.lt/butai/vilniuje/puslapis/"
            + str(page_count)
            + "/?change_region=1#searchFilterPage"
        )
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        # extracting prices
        prices = [
            int(price.text.split(" €")[0].split("\n")[1].replace(" ", ""))
            for price in soup.find_all("span", class_="item-price-main-v3")
        ]

        # extracting districs
        districts = [
            district.text.split(",")[0].split()[-1]
            for district in soup.find_all("span", class_="item-address-v3")
        ]

        # extracting room number
        num_rooms = [
            int(rooms.text.split(" rooms")[0].split()[-1])
            for rooms in soup.find_all("span", class_="item-description-v3")
        ]

        # extracting area size
        area = [
            float(area.text.split("rooms, ")[1].split(" m²,")[0].replace(",", "."))
            for area in soup.find_all("span", class_="item-description-v3")
        ]

        # extracting years when objects were built
        built = [
            int(year.text.split(" year,")[0].split(", ")[-1])
            for year in soup.find_all("span", class_="item-description-v3")
        ]

        # extracting heating systems
        heating = [
            heating.text.split(", ")[-2]
            for heating in soup.find_all("span", class_="item-description-v3")
        ]

        # extracting completeness
        completeness = [
            completeness.text.split(", ")[-1].split("  ")[0]
            for completeness in soup.find_all("span", class_="item-description-v3")
        ]
        # checking if all lists have the same lenght:
        if (
            len(prices)
            == len(districts)
            == len(num_rooms)
            == len(area)
            == len(built)
            == len(heating)
            == len(completeness)
        ):
            prices_list.extend(prices)
            districts_list.extend(districts)
            num_rooms_list.extend(num_rooms)
            area_list.extend(area)
            built_years_list.extend(built)
            heating_list.extend(heating)
            completeness_list.extend(completeness)

        # delay in order to prevent from robots buster
        time.sleep(2)

        # switching page
        page_count += 1

    # creating dictionary and slicing lists
    apartments_dict = {
        "num_rooms": num_rooms_list[:expected_items],
        "area": area_list[:expected_items],
        "years_built": built_years_list[:expected_items],
        "heating": heating_list[:expected_items],
        "completeness": completeness[:expected_items],
        "district": districts_list[:expected_items],
        "price": prices_list[:expected_items],
    }

    # creating dataframe
    apartments_df = pd.DataFrame.from_dict(apartments_dict)

    return apartments_df