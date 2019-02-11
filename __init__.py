import requests
from lxml import html
import re
import cfscrape


class ProxiesFetcher:

    def __init__(self):
        self.useless_variable = None

    def default():
        return self.hidemyna()


    def freeproxylist(number=None):
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = html.fromstring(response.text)
        proxies = []
        for i, tr in enumerate(parser.xpath('//tbody/tr')[:20]):
            if tr.xpath('.//td[7][contains(text(),"yes")]'):
                #Grabbing IP and corresponding PORT
                proxy = ":".join([tr.xpath('.//td[1]/text()')[0], tr.xpath('.//td[2]/text()')[0]])
                proxies.append(proxy)

            if number and i >= number-1:  # to be tested
                break

        return proxies




    def hidemyna(number=None, anonymity=None, http = True, https = False):
        url = 'https://hidemyna.me/en/proxy-list/?'



        if anonymity and 1 <= anonymity and anonymity <= 4:
                anonymity_maxtime = {
                    0: 200,
                    1: 250,
                    2: 2000,
                    3: 1000,
                    4: 350
                }
                url += '&maxtime=' + str(anonymity_maxtime[anonymity])
        else:
            url += '&maxtime=200'

        url += '&type='
        if http: url += 'h'
        if https: url += 's'


        if anonymity and 1 <= anonymity and anonymity <= 4:  # this needs to be done seperately so that hidemyna doesn't detect that this is a bot
            url += '&anon=' + str(anonymity)

        url += '#list'  # not required, but naturally generated user requests include it

        scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
        # Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
        body = scraper.get(url).content
        tree = html.fromstring(body)
        tr_elements = tree.xpath('//table[@class="proxy-table" or @class="proxy__t"]/tbody/tr')

        proxies = []

        for i, tr_element in enumerate(tr_elements):
            ip = tr_element.xpath('.//td[1]/text()')[0]
            port = tr_element.xpath('.//td[2]/text()')[0]
            proxy = ip + ':' + port

            if re.match('\d+\.\d+\.\d+\.\d+:\d{2,5}', proxy):
                proxies.append(proxy)

            if number and i >= number-1:  # to be tested
                break

        return proxies


    def limit(input_list, limit):
        return input_list[:limit]


    def manual_list():
        return [
            "41.50.80.237:30534",
            "41.180.65.27:60840",
            "41.217.242.11:40131",
            "196.250.23.70:8080",
            "41.164.169.50:59477",
            "41.242.166.233:53112"
        ]


