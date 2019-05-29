# Proxies Fetcher
Fetches live proxies for webscraping purposes. In Python.

In development.

Cloudfare keeps creating new algorithms, which stops this module from scraping _hidemyna_. Thus, ensure you have the absolute latest version of `cfscrape` installed.

### Use
The module has 3 functions: `default`, `hidemyna` and `freeproxylist`
Calling any of the this module's functions will return a lists of proxies (IP's with port numbers). It does this by crawling websites with free proxies. Different methods relate to different sites. Some allow optional parameters (such as HTTPS proxies).
