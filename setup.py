from setuptools import setup

setup(
   name='proxiesfetcher',
   version='0.1',
   description='Fetches live proxies for webscraping purposes',
   author='Chrisjan Wust',
   author_email='chrisjanwust@gmail.com',
   packages=['proxiesfetcher'],
   install_requires=['cfscrape', 'requests', 'lxml'], #external packages as dependencies
)