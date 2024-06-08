# from celery import shared_task
# from .models import ScrapeJob
# from crypto_scraper.coinmarketcap import CoinMarketCap
#
#
# @shared_task
# def scrape_coin_data(job_id, coins):
#     job = ScrapeJob.objects.get(job_id=job_id)
#     results = []
#
#     scraper = CoinMarketCap()
#
#     for coin in coins:
#         data = scraper.get_coin_data(coin)
#         if data:
#             results.append({
#                 'coin': coin,
#                 'output': data
#             })
#         else:
#             results.append({
#                 'coin': coin,
#                 'output': 'Error retrieving data'
#             })
#
#     job.status = 'COMPLETED'
#     job.result = results
#     job.save()
#


# api/tasks.py

import logging
from celery import shared_task
from .models import ScrapeJob
from crypto_scraper.coinmarketcap import CoinMarketCap

logger = logging.getLogger(__name__)

@shared_task
def scrape_coin_data(job_id, coins):
    logger.info(f"Starting scrape_coin_data task with job_id: {job_id} and coins: {coins}")
    job = ScrapeJob.objects.get(job_id=job_id)
    results = []

    scraper = CoinMarketCap()

    for coin in coins:
        logger.info(f"Scraping data for coin: {coin}")
        data = scraper.get_coin_data(coin)
        if data:
            logger.info(f"Successfully scraped data for coin: {coin}")
            results.append({
                'coin': coin,
                'output': data
            })
        else:
            logger.error(f"Error retrieving data for coin: {coin}")
            results.append({
                'coin': coin,
                'output': 'Error retrieving data'
            })

    job.status = 'COMPLETED'
    job.result = results
    job.save()
    logger.info(f"Completed scrape_coin_data task with job_id: {job_id}")
