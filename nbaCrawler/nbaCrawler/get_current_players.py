from urllib2 import urlopen

def get_current_players():
	local = open('/home/salman/NBA-Players-Database-Website/nbaCrawler/nbaCrawler/current_players.xml', 'w')
	local.write(urlopen('http://www.nba.com/current_players.xml').read())
	local.close()

if __name__ == '__main__':
	get_current_players()