from typing import Union

from fastapi import FastAPI, Query
import requests
import urllib.request
import re
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from datetime import date
import calendar
import warnings
warnings.filterwarnings("ignore")
import copy
from collections import Counter
from itertools import chain

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def get_dates():
    end_date = str(date.today().strftime("%d/%m/%Y"))
    today = date.today()
    day = today.day
    month = today.month - 1 if today.month > 1 else 12
    year = today.year if today.month > 1 else today.year - 1

    # Adjust the day if necessary
    last_day_of_prev_month = calendar.monthrange(year, month)[1]
    if day > last_day_of_prev_month:
        day = last_day_of_prev_month

    prev_month_date = date(year, month, day)
    start_date = prev_month_date.strftime("%d/%m/%Y")
    return start_date, end_date

@app.get("/news/")
async def read_article(ticker: str = Query(default = "bbca"), dateStart: str = Query(default = get_dates()[0]), dateEnd: str = Query(default = get_dates()[1])):
    new_list = get_links(ticker=ticker, start_date = dateStart, end_date=dateEnd)
    print(new_list)
    response = await main(new_list)
    return response

def get_links(ticker: str = "bbca", start_date: str = get_dates()[0], end_date: str = get_dates()[1]):
    base_url = f'https://www.detik.com/search/searchnews?query={ticker}&result_type=latest&fromdatex={start_date}&todatex={end_date}'
    response = requests.get(base_url)
    html_soup = BeautifulSoup(response.text, "html.parser")
    news_list = html_soup.find_all("h3", {"class": "media__title"})
    new_news = []
    for index, news in enumerate(news_list):
        pattern = r'href="([^"]+)"'

        # Search for the pattern in the HTML
        match = re.findall(pattern, str(news))

        if match:
            new_news.append(match)
    news_list = list(chain.from_iterable(new_news))
    return news_list

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        responses = await asyncio.gather(*tasks)
        return responses

def parse_news(responses):
    detailed_news = []
    # Define the regex pattern
    pattern = re.compile(r'<p>(.*?)</p>', re.DOTALL)

    for response in responses:
        soup_detailed_news = BeautifulSoup(response, "html.parser")
        # Find all matches
        matches = pattern.findall(str(soup_detailed_news))

        # Clean up the matches to remove any additional HTML tags within the paragraphs
        cleaned_matches = [re.sub(r'<.*?>', '', match).strip() for match in matches]
        detailed_news.append((" ".join(cleaned_matches)))

        # Print the cleaned matches
        # for match in cleaned_matches:
        #     detailed_news.append(("".join(cleaned_matches)))
    return detailed_news

async def main(news_list):
    responses = await fetch_all(news_list)
    detailed_news = parse_news(responses)
    return detailed_news