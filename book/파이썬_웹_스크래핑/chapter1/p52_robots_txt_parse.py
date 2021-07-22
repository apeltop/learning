from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url('https://www.google.com/robots.txt')
rp.read()

url = 'https://www.google.com/'
user_agent = 'BadCrawler'
print(rp.can_fetch(user_agent, url))

user_agent = 'GoodCrawler'
print(rp.can_fetch(user_agent, url))