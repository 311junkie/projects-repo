from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)

driver.get("http://fin.bdo.com")
#driver.find_element_by_name("q").send_keys("python selenium")
#driver.find_element_by_partial_link_text("BDO Sign In").click()
#elements = driver.find_elements_by_partial_link_text("")
#links = driver.find_element_by_css_selector('span.ps-link').click()
driver.find_element_by_id('pswrapper')
#for link in links:
#    print (link)    # id name as string
#print(links)
driver.close()