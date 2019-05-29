# Proxies Fetcher
Python module that fetches live proxies for webscraping purposes.


### Requirements
* `cfscrape`. Cloudfare keeps creating new algorithms, which stops this module from scraping _hidemyna_. Thus, ensure you have the absolute latest version installed.
* `lmxl`
* `requests`

### Use
Calling any of the this module's functions will return a lists of proxies (IP's with port numbers). It does this by crawling websites with free proxies. Different methods relate to different sites.

* `hidemyna` uses `https://hidemyna.me/en/proxy-list`
* `freeproxylist` uses `https://free-proxy-list.net/`
* `default` employs one of the other functions - whichever is working best at the moment.

Some allow optional parameters (such as HTTPS proxies or requesting a certain number of proxies).
