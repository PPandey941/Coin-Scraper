import requests
from bs4 import BeautifulSoup
import re

class CoinMarketCap:
    BASE_URL = 'https://coinmarketcap.com/currencies/'

    def get_coin_data(self, coin):
        url = f'{self.BASE_URL}{coin}/'
        response = requests.get(url)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        data = self._parse_coin_page(soup)
        return data

    def _parse_coin_page(self, soup):
        def extract_number(text):
            return float(re.sub(r'[^\d.]+', '', text))

        try:
            price = extract_number(soup.select_one('.sc-d1ede7e3-0.fsQm.base-text').text)
            price_change = extract_number(soup.select_one('.sc-71024e3e-0.sc-58c82cf9-1.bgxfSG.iPawMI').text)
            market_cap = extract_number(soup.select_one('.sc-d1ede7e3-0.hPHvUM.base-text .sc-4c05d6ef-0.dMwnWW').text)
            market_cap_rank = int(soup.select_one('.text.slider-value.rank-value').text[1:])
            volume = extract_number(soup.select('dd.sc-d1ede7e3-0.hPHvUM.base-text')[1].text)
            volume_rank = int(soup.select('.text.slider-value.rank-value')[1].text[1:])
            volume_change = extract_number(soup.select('dd.sc-d1ede7e3-0.hPHvUM.base-text')[2].text)
            circulating_supply = extract_number(soup.select('dd.sc-d1ede7e3-0.hPHvUM.base-text')[3].text)
            total_supply = extract_number(soup.select('dd.sc-d1ede7e3-0.hPHvUM.base-text')[4].text)
            diluted_market_cap = extract_number(soup.select('dd.sc-d1ede7e3-0.hPHvUM.base-text')[5].text)

            contracts = [
                {
                    'name': 'solana',
                    'address': soup.select_one('span.sc-71024e3e-0.eESYbg.address').text.strip()
                }
            ]

            official_links = [
                {
                    'name': 'website',
                    'link': soup.select_one('a[rel="nofollow noopener"][href*="dukocoin.com"]').get('href')
                }
            ]

            socials = [
                {
                    'name': 'twitter',
                    'url': soup.select_one('a[rel="nofollow noopener"][href*="twitter.com"]').get('href')
                },
                {
                    'name': 'telegram',
                    'url': soup.select_one('a[rel="nofollow noopener"][href*="t.me"]').get('href')
                }
            ]

            return {
                'price': price,
                'price_change': price_change,
                'market_cap': market_cap,
                'market_cap_rank': market_cap_rank,
                'volume': volume,
                'volume_rank': volume_rank,
                'volume_change': volume_change,
                'circulating_supply': circulating_supply,
                'total_supply': total_supply,
                'diluted_market_cap': diluted_market_cap,
                'contracts': contracts,
                'official_links': official_links,
                'socials': socials
            }
        except Exception as e:
            return {'error': str(e)}
