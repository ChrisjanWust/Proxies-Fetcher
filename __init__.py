import requests
from lxml import html
import re
import cfscrape



class ProxiesFetcher:


    def default(self):
        return self.hidemyna()


    @staticmethod
    def freeproxylist(number=None):
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = html.fromstring(response.text)
        proxies = []
        for i, tr in enumerate(parser.xpath('//tbody/tr')[:]):
            # if tr.xpath('.//td[7][contains(text(),"yes")]'):  # could implement https only searching using this column
            ip = tr.xpath('.//td[1]/text()')[0]
            port = tr.xpath('.//td[2]/text()')[0]
            proxy = ip + ':' + port
            if re.match('\d+\.\d+\.\d+\.\d+:\d+', proxy):
                proxies.append(proxy)
            if number and i >= number-1:
                break
        return proxies


    @staticmethod
    def hidemyna(number=None, anonymity=None, http=True, https=False):
        url = 'https://hidemyna.me/en/proxy-list/?'  # parameters will be added
        # limits max time to only include fast proxies. The limit is varied according to the typical performance for the level of anonymity
        if anonymity and 1 <= anonymity and anonymity <= 4:
                anonymity_maxtime = {
                    0: 400,
                    1: 450,
                    2: 2000,
                    3: 1000,
                    4: 550
                }
                url += '&maxtime=' + str(anonymity_maxtime[anonymity])
        else:
            url += '&maxtime=400'

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
            if number and i >= number - 1:
                break
        return proxies




if __name__ == '__main__':
    functions = [ProxiesFetcher.freeproxylist, ProxiesFetcher.hidemyna]
    for function in functions:
        proxies = function()
        print(f"{len(proxies)} proxies returned by {function.__name__}")
        print(f"Sample:\t{str(proxies[:3])[:-1]}, ... ]")
        if len(proxies) >= 20:
            print(f"Function {function.__name__} seems to be working fine.")
        else:
            print(f"Function {function.__name__} doesn't seem to be operational.")
        print()
