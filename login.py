import time
from selenium import webdriver
 
def login_mail(username, password):
	driver = webdriver.Chrome()
	browser.get('https://mail.pku.edu.cn/')
	browser.find_by_id('username').fill(username)
	browser.find_by_id('password').fill(password)
	browser.find_by_id('login_button').click()
	time.sleep(5)
	browser.quit()
	
if __name__ == '__main__':
	login_mail('2101210560', 'dzn-0419')
