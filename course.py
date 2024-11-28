import requests as r
from bs4 import BeautifulSoup


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'utf-8',
    'accept-language': 'uk,en-US;q=0.9,en;q=0.8,ru;q=0.7',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

s = r.Session()


def dollar():

    global dolres

    dolres = s.get('https://www.bloomberg.com/quote/USDRUB:CUR', headers=headers)
    print(dolres.text)
    soup = BeautifulSoup(dolres.text, 'html.parser')

    usd = soup.select("#__next > div > div.media-ui-LeaderboardAd_parallaxWrapper-JMVgdxR--aU- > div.layout_gridLayoutContainer__0tUIV > div > main > div > div:nth-child(1) > div.quotePageLayout_currentPriceEmptyAfterHours__FN1wU > div.currentPrice_currentPriceContainer__nC8vw > div.sized-price.media-ui-SizedPrice_extraLarge-05pKbJRbUH8-")
    usd_change = soup.select("#__next > div > div.media-ui-LeaderboardAd_parallaxWrapper-JMVgdxR--aU- > div.layout_gridLayoutContainer__0tUIV > div > main > div > div:nth-child(1) > div.quotePageLayout_currentPriceEmptyAfterHours__FN1wU > div.currentPrice_currentPriceContainer__nC8vw > div.media-ui-Change_change-lMq4LV-1csY-.media-ui-Change_large--d--nglkh5o-.media-ui-Change_refresh2024-EajM9IkrlnU-.currentPrice_change__zZt9P.change > span > span > span")

    usd = BeautifulSoup(str(usd), 'html.parser').get_text()[1:-1]
    usd_change = BeautifulSoup(str(usd_change), 'html.parser').get_text()[1:-1]

    return usd, usd_change

def euro():  
    eurres = s.get('https://www.bloomberg.com/quote/EURRUB:CUR', headers=headers)
    soup = BeautifulSoup(eurres.text, 'html.parser')

    eur = soup.select("#__next > div > div.media-ui-LeaderboardAd_parallaxWrapper-JMVgdxR--aU- > div.layout_gridLayoutContainer__0tUIV > div > main > div > div:nth-child(1) > div.quotePageLayout_currentPriceEmptyAfterHours__FN1wU > div.currentPrice_currentPriceContainer__nC8vw > div.sized-price.media-ui-SizedPrice_extraLarge-05pKbJRbUH8-")
    eur_change = soup.select("#__next > div > div.media-ui-LeaderboardAd_parallaxWrapper-JMVgdxR--aU- > div.layout_gridLayoutContainer__0tUIV > div > main > div > div:nth-child(1) > div.quotePageLayout_currentPriceEmptyAfterHours__FN1wU > div.currentPrice_currentPriceContainer__nC8vw > div.media-ui-Change_change-lMq4LV-1csY-.media-ui-Change_large--d--nglkh5o-.media-ui-Change_refresh2024-EajM9IkrlnU-.currentPrice_change__zZt9P.change > span > span > span")

    eur = BeautifulSoup(str(eur), 'html.parser').get_text()[1:-1]
    eur_change = BeautifulSoup(str(eur_change), 'html.parser').get_text()[1:-1]

    return eur, eur_change


print(f"Текущий курс доллара: {dollar()[0]}. Динамика изменения цены за сутки: {dollar()[1]}")
print(f"Текущий курс евро: {euro()[0]}. Динамика изменения цены за сутки: {euro()[1]}")
