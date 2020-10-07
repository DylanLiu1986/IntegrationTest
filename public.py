from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login():
	def user_login(self,driver):

		driver.find_element_by_class_name("login-link").click()

		element=WebDriverWait(driver,5,0.5).until(
			EC.presence_of_element_located((By.ID, "auth_key"))
			)

		element.clear()
		element.send_keys("254795610@163.com")
		driver.find_element_by_class_name("submit-field").click()
		driver.find_element_by_name("password").send_keys("liudalu@2011")
		driver.find_element_by_class_name("submit-field").click()
		driver.find_element_by_partial_link_text("个人账户").click()

		element=WebDriverWait(driver,5,0.5).until(
			EC.presence_of_element_located((By.ID, "create_new"))
			)


class delete():
	def delete_form(self,driver,form_name,edit_form_url):
		driver.get(edit_form_url)
		element = WebDriverWait(driver, 10).until(     
			EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[8]/a[3]"))
			) 
		delete_bttton=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[8]/a[3]")
		driver.execute_script("$(arguments[0]).click()",delete_bttton)

		element = WebDriverWait(driver, 10).until(     
			EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[8]/div[3]/div/div/div[2]/div/input"))
			) 
		driver.find_elements_by_css_selector("[class='gd-input-large confirm-input']")[1].clear()
		driver.find_elements_by_css_selector("[class='gd-input-large confirm-input']")[1].send_keys(form_name)
		driver.find_elements_by_css_selector("[class='gd-btn gd-btn-danger submit confirm']")[1].click()
