import json
import requests
from bs4 import BeautifulSoup

def get_product_price_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    req = requests.get(url)
    scrap = BeautifulSoup(req.content, "html.parser")
    data_components_str = scrap.select_one('.cardRoot[data-components]')['data-components']
    data_components = json.loads(data_components_str)
    product_price = data_components['1']['price']['displayString']
    return url, product_price

def get_product_price_ebay(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    req = requests.get(url)
    scrap = BeautifulSoup(req.content, "html.parser")
    x_price_primary_div = scrap.find('div', class_='x-price-primary')
    product_price = x_price_primary_div.find('span', class_='ux-textspans').text.strip()
    return url, product_price

# Example usage:
amazon_url = "https://www.amazon.com/dp/B0BZ9T8R41?ref_=cm_sw_r_cso_wa_apin_dp_J5HXW88F25VBSHWMXY9P&cafHiResImg=1&language=en-US&th=1"
ebay_url = "https://www.ebay.com/itm/325661593466?mkcid=16&mkevt=1&mkrid=711-127632-2357-0&ssspo=1PO9jDhpTTO&sssrc=4429486&ssuid=8jcvtrvssmq&var=&widget_ver=artemis&media=WHATS_APP"

website, amazon_product_price = get_product_price_amazon(amazon_url)
ebay_website, ebay_product_price = get_product_price_ebay(ebay_url)

