BOT_NAME = "blog"
SPIDER_MODULES = ["blog.spiders"]
NEWSPIDER_MODULE = "blog.spiders"


# Get API Key at https://account.proxy-port.com/scraping
PROXY_PORT_API_KEY = ''

DOWNLOADER_MIDDLEWARES = {
    'scrapyproxyport.middlewares.ProxyMiddleware': 898,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 899,
}
DOWNLOAD_TIMEOUT = 10
RETRY_TIMES = 20
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'
