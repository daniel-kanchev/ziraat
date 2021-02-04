BOT_NAME = 'ziraatbank'
SPIDER_MODULES = ['ziraatbank.spiders']
NEWSPIDER_MODULE = 'ziraatbank.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
   'ziraatbank.pipelines.DatabasePipeline': 300,
}
LOG_LEVEL = 'WARNING'
