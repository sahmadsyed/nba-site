import scrapy
from nbaCrawler.items import StatsCrawler

class StatsSpider(scrapy.Spider):
	name = 'StatsSpider'
	allow_domains = ['http://en.wikipedia.org/']
	start_urls = ['http://en.wikipedia.org/wiki/Andrew_Wiggins'] #, 'http://en.wikipedia.org/wiki/Ben_Wallace', 'http://en.wikipedia.org/wiki/Nate_Robinson', 'http://en.wikipedia.org/wiki/Tracy_McGrady']

	def parse(self,response):
		player_name = response.xpath('//title/text()').extract()[0]
		player_name = player_name[:player_name.find(' - Wikipedia, the free encyclopedia')]
		if '(' in player_name:
			player_name = player_name[:player_name.find('(') - 1]
		# first_space = player_name.index(' ')
		# first_name = player_name[0:first_space]
		# second_space = player_name.index(' ', first_space + 1)
		# last_name = player_name[first_space + 1: second_space]

		resp = response.xpath('//span[@id = "Regular_season"]/text()|//table[@class = "wikitable sortable"]//td/a/text()|//table[@class = "wikitable sortable"]//td/text()|//table[@class = "wikitable sortable"]//td/b/text()')

		reg_index = -1
		for i in resp:
			try:
				if i.extract() == 'Regular season':
					reg_index = resp.index(i)
					break
			except:
				continue
		if reg_index == -1:
			return
		resp = resp[reg_index + 1:]
		stats_end = False
		count = 0

		while not stats_end:
			stats_item = StatsCrawler()
			stats_item['name'] = unicode(player_name)
			#stats_item['first_name'] = first_name
			#stats_item['last_name'] = last_name

			if resp[count].extract() == 'Career':
				stats_item['season'] = 'Career'
				stats_item['team'] = 'Career'
				stats_end = True
				count-= 1
			else:
				stats_item['season'] = resp[count].extract()[0:4]
				if resp[count + 1].extract() == u'\u2020':
					count+= 1
				stats_item['team'] = resp[count + 1].extract()
			
			stats_item['gp'] = resp[count + 2].extract()
			stats_item['gs'] = resp[count + 3].extract()
			stats_item['mpg'] = resp[count + 4].extract()
			stats_item['fg'] = resp[count + 5].extract()
			stats_item['tfg'] = resp[count + 6].extract()
			stats_item['ft'] = resp[count + 7].extract()
			stats_item['rpg'] = resp[count + 8].extract()
			stats_item['apg'] = resp[count +  9].extract()
			stats_item['spg'] = resp[count + 10].extract()
			stats_item['bpg'] = resp[count + 11].extract()
			stats_item['ppg'] = resp[count + 12].extract()
			count+=13
			yield stats_item
		



