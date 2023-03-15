The Scrapy sample project illustrates the use of the [scrapyproxyport](https://github.com/proxyport/scrapy-proxyport) middleware

## Prerequisites
To run this project you will need a free API key. Get your API key <a href="https://account.proxy-port.com/scraping" target="_blank">here</a>.
Detailed instructions <a href="https://proxy-port.com/en/scraping-proxy/getting-started" target="_blank">here</a>.

## Installation

```shell
$ git clone https://github.com/proxyport/scrapy-proxyport-example
$ cd scrapy-proxyport-example
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.pip
```

## Set API Key

Open `scrapy-proxyport-example/blog/blog/settings.py` and set [your API Key](https://account.proxy-port.com/scraping) to `PROXY_PORT_API_KEY` variable.

```python
PROXY_PORT_API_KEY = '<API_KEY>'
```

## Run spider

```shell
$ source env/bin/activate
$ cd blog
$ scrapy crawl blogspider
```
