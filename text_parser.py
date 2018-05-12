# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome("chromedriver.exe")
def add():
	print("HI0")
add()
def textParser():	
	print("HI")
	import  re
	pattern = r"([A-Z]+)(\d+)([A-Z]+)"
	frolls = open('namesandnumbers.txt','r')
	string = frolls.read()
	print string
	matches = re.findall(pattern, string, flags=0)
	matches_final = [''.join(match) for match in matches]
	pattern = r"([a-z]+)(\d+)([a-z]+)"
	matches = re.findall(pattern, string, flags=0)
	matches_final += [''.join(match) for match in matches]
	print matches_final
textParser()

