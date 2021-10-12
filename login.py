import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
def login_mail(username, password):
	chrome_options = Options()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--headless')
	browser = webdriver.Chrome(chrome_options=chrome_options)

	browser.get('https://mail.pku.edu.cn/')
	browser.find_element_by_id('username').send_keys(username)
	browser.find_element_by_id('password').send_keys(password)
	browser.find_element_by_id('login_button').click()
	time.sleep(1)
	browser.quit()
	print('user ' + username + ' logged in.')
	
if __name__ == '__main__':
	users = os.environ["USERS"]
	users = eval(users)
	for user in users:
		login_mail(user[0], user[1])

