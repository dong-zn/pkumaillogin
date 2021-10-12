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
	browser.find_by_id('username').fill(username)
	browser.find_by_id('password').fill(password)
	browser.find_by_id('login_button').click()
	time.sleep(5)
	browser.quit()
	
if __name__ == '__main__':
	login_mail('2101210560', 'dzn-0419')
