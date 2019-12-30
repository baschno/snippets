import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer

START_TIME = default_timer()


async def fetch(session, csv):
    base_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/"
    url = "{}{}".format(base_url, csv)
    async with session.get(url) as response:
        data = await response.text()
        if response.status != 200:
            print("FAILURE::{0}".format(url))

        elapsed = default_timer() - START_TIME
        time_completed_at = "{:5.2f}s".format(elapsed)
        print("{0:<30} {1:>20}".format(csv, time_completed_at))

        return data


async def get_data_asynchronous():
    csvs_to_fetch = [
        "ford_escort.csv",
        "cities.csv",
        "hw_25000.csv",
        "mlb_teams_2012.csv",
        "nile.csv",
        "homes.csv",
        "hooke.csv",
        "lead_shot.csv",
        "news_decline.csv",
        "snakes_count_10000.csv",
        "trees.csv",
        "zillow.csv"
    ]
    tasks = []
    print("{0:<30} {1:>20}".format("File", "Completed at"))
    async with aiohttp.ClientSession() as session:
        for csv in csvs_to_fetch:
            task = asyncio.ensure_future(fetch(session, csv))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_data_asynchronous())
    loop.run_until_complete(future)
