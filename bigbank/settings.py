BOT_NAME = 'bigbank'

SPIDER_MODULES = ['bigbank.spiders']
NEWSPIDER_MODULE = 'bigbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bigbank.pipelines.BigbankPipeline': 100,

}