import requests
from lxml import html
import re
import cfscrape
import asyncio
import lxml



def get_proxies():
    return get_proxies_freeproxylist()


def get_proxies_freeproxylist():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = html.fromstring(response.text)
    proxies = []
    for tr in parser.xpath('//tbody/tr')[:20]:
        if tr.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([tr.xpath('.//td[1]/text()')[0], tr.xpath('.//td[2]/text()')[0]])
            proxies.append(proxy)

    return proxies


# unsuccessful. hidemyna.me checks for robots
def get_proxies_hidemyna_try1():
    url = 'https://hidemyna.me/en/proxy-list/?maxtime=800&type=s&anon=34'
    print("Requesting " + url)
    response = requests.get(url)
    parser = html.fromstring(response.text)
    proxies = []
    for tr in parser.xpath('//tbody/tr')[:50]:
        proxy_ip = tr.xpath('./td[1]/text()')[0]
        print ("Proxy ip found:\t" + proxy_ip)
        if proxy_ip:
            if re.match('\d+\.\d+\.\d+\.\d+', proxy_ip):
                proxy_port = tr.xpath("./td[2]/text()")[0]
                print("Proxy port found:\t" + proxy_port)
                if re.match("\d{2,5}", proxy_port):
                    proxy = proxy_ip + ":" + proxy_port
                    proxies.append(proxy)

    return proxies



def get_proxies_hidemyna_try2():
    url = 'https://hidemyna.me/en/proxy-list/?maxtime=800&type=s&anon=34'
    scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
    # Or: scraper = cfscrape.CloudflareScraper()  # CloudflareScraper inherits from requests.Session
    body = scraper.get(url).content
    tree = html.fromstring(body)
    tr_elements = tree.xpath('//table[@class="proxy-table" or @class="proxy__t"]/tbody/tr')

    proxies = []

    for tr_element in tr_elements:
        ip = tr_element.xpath('.//td[1]/text()')[0]
        port = tr_element.xpath('.//td[2]/text()')[0]
        proxy = ip + ':' + port

        if re.match('\d+\.\d+\.\d+\.\d+:\d{2,5}', proxy):
            proxies.append(proxy)

    return proxies


def get_proxies_hidemyna_manual():
    return [
        "199.21.97.54:80",
        "199.21.97.220:80",
        "199.21.96.145:80",
        "199.21.96.78:80",
        "199.21.97.175:80",
        "199.21.98.101:80",
        "199.21.96.80:80",
        "199.21.96.99:80",
        "199.21.96.70:80",
        "199.21.96.48:80",
        "199.21.97.130:80",
        "199.21.99.109:80",
        "199.21.97.210:80",
        "199.21.98.8:80",
        "199.21.99.192:80",
        "199.21.97.2:80",
        "199.21.99.183:80",
        "199.21.99.233:80",
        "199.21.96.54:80",
        "199.21.96.47:80",
        "199.21.98.32:80",
        "35.233.106.236:3128",
        "199.21.98.172:80",
        "199.21.99.163:80",
        "199.21.98.130:80",
        "199.21.97.61:80",
        "199.21.97.196:80",
        "199.21.98.61:80",
        "199.21.98.129:80",
        "199.21.96.173:80",
        "199.21.96.224:80",
        "199.21.99.207:80",
        "199.21.99.198:80",
        "199.21.96.75:80",
        "199.21.98.29:80",
        "199.21.97.177:80",
        "199.21.97.26:80",
        "199.21.97.55:80",
        "199.21.97.59:80",
        "199.21.98.110:80",
        "199.21.96.178:80",
        "199.21.97.172:80",
        "199.21.98.52:80",
        "199.21.97.239:80",
        "199.21.96.87:80",
        "199.21.97.74:80",
        "199.21.97.80:80",
        "199.21.97.8:80",
        "199.21.99.89:80",
        "199.21.98.200:80",
        "199.21.97.97:80",
        "199.21.96.241:80",
        "199.21.97.75:80",
        "199.21.99.118:80",
        "199.21.97.229:80",
        "199.21.98.119:80",
        "199.21.99.93:80",
        "199.21.99.135:80",
        "199.21.98.18:80",
        "199.21.99.140:80",
        "199.21.98.131:80",
        "199.21.96.4:80",
        "199.21.96.31:80",
        "199.21.98.134:80",
        "199.21.99.16:80",
        "199.21.97.104:80",
        "199.21.98.169:80",
        "199.21.99.27:80",
        "138.68.161.60:3128",
        "199.21.98.88:80",
        "199.21.98.84:80",
        "199.21.97.247:80",
        "138.68.120.201:3128",
        "199.21.98.136:80",
        "207.154.231.213:3128",
        "199.21.96.32:80",
        "199.21.98.124:80",
        "199.21.97.45:80",
        "142.93.38.72:8080",
        "94.130.98.54:8888",
        "88.99.242.188:3128",
        "104.248.161.99:8080",
        "104.248.170.69:8080",
        "195.201.109.177:80",
        "104.248.169.58:8080",
        "5.189.172.203:3128",
        "51.75.65.79:8080",
        "195.201.224.177:3128",
        "173.212.202.65:80",
        "138.197.191.177:8888",
        "173.249.43.105:3128",
        "104.248.169.58:8080",
        "5.189.172.203:3128",
        "51.75.65.79:8080",
        "138.68.161.157:8080",
        "173.212.198.198:8080",
        "207.154.231.213:8080",
        "173.249.35.163:10010",
        "104.248.166.0:8080",
        "5.189.144.198:3128",
        "5.189.133.231:80",
        "78.47.157.159:80",
        "138.68.161.157:3128",
        "138.68.161.60:8080",
        "173.212.229.220:80",
        "173.249.51.179:3128",
        "104.248.30.172:80",
        "46.5.252.70:8080",
        "178.33.39.70:3128",
        "88.99.242.130:3128",
        "5.189.177.94:10010",
        "173.249.43.105:3128",
        "138.201.223.250:31288",
        "94.130.20.85:31288",
    ]