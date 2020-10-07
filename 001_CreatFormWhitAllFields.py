from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public import *
from time import sleep


driver=webdriver.Chrome()
driver.get("https://www.jinshuju.net")

#登录
login().user_login(driver)

#创建空白表单
driver.find_element_by_id("create_new").click()

element=WebDriverWait(driver,10,0.5).until(
	EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div/div[1]/div[2]/div/div/div[8]/div"))
	)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div[1]/div[2]/div/div/div[8]/div").click()

element=WebDriverWait(driver,10,0.5).until(
	EC.presence_of_element_located((By.CLASS_NAME, "blank-form-create"))
	)
driver.find_element_by_class_name("blank-form-create").click()

element=WebDriverWait(driver,10,0.5).until(
	EC.presence_of_element_located((By.ID, "form-setting__save-button"))
	)

#添加标题
element = WebDriverWait(driver, 10).until(     
	EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/form/div[1]/div[2]/div[1]/div/div[1]/div"))
	) 
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/form/div[1]/div[2]/div[1]/div/div/div/input").clear()

driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/form/div[1]/div[2]/div[1]/div/div/div/input").send_keys("全字段表单集成测试")


#添加通用字段
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[1]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[3]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[4]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[7]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[8]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[9]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[10]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[11]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[12]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[13]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[2]/span[1]/div/div/div[14]/a").click()

#添加描述分页字段
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[3]/span[1]/div/div/div[1]/a").click()

#添加联系信息字段
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[5]/span[1]/div/div/div[1]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[5]/span[1]/div/div/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[5]/span[1]/div/div/div[3]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[5]/span[1]/div/div/div[4]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[5]/span[1]/div/div/div[5]/a").click()


#添加高级字段字段
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[6]/span[1]/div/div/div[1]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[6]/span[1]/div/div/div[2]/a").click()
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[6]/span[1]/div/div/div[4]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[6]/span[1]/div/div/div[5]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[6]/span[1]/div/div/div[6]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div[6]/span[1]/div/div/div[7]/a").click()

#保存表单
driver.find_element_by_id("form-setting__save-button").click()
element = WebDriverWait(driver, 10).until(     
	EC.element_to_be_clickable((By.ID, "to_publish_btn"))
	) 

# 打开表单发布页面
driver.find_element_by_id("to_publish_btn").click()
element = WebDriverWait(driver, 10).until(     
	EC.element_to_be_clickable((By.CLASS_NAME, "published-form__qr-part"))
	) 
driver.find_element_by_xpath("/html/body/div[17]/div/div/div[2]/div/div[1]/div[1]/div[2]/section/div[3]/div[2]/a[2]").click()
windows=driver.window_handles
driver.switch_to.window(windows[-1])

# 填写表单
#单行文字、多行文字、单选、多选

driver.find_elements_by_tag_name("input")[0].send_keys("单行文字")
driver.find_elements_by_tag_name("input")[1].send_keys("多行文字")
driver.find_elements_by_tag_name("input")[2].click()
driver.find_elements_by_tag_name("input")[3].click()
driver.find_elements_by_tag_name("input")[4].click()

# 下拉框
driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/div/div[10]/div/div[2]/div/div/span/div/div/div/div[1]/div[1]").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/div/div[10]/div/div[2]/div/div/span/div/div/div/div[2]/div/div[1]").click()

# 勾选同意
driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[5]/label").click()

# 提交表单
driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[6]/div[1]/button").click()
element = WebDriverWait(driver, 10).until(     
	EC.element_to_be_clickable((By.CLASS_NAME, "gd-icon-check-circle"))
	) 

# 删除表单
success_url=driver.current_url
edit_form_url=("https://jinshuju.net/forms/"+success_url[23:29])
delete().delete_form(driver,"全字段表单集成测试",edit_form_url)
element = WebDriverWait(driver, 10).until(     
	EC.element_to_be_clickable((By.ID, "dashboard_breadcrumbs"))
	) 

# 关闭页面
driver.quit()






