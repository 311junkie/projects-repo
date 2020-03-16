from selenium import webdriver
import os
import time


#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.set_page_load_timeout(10)
driver.maximize_window()

#print(os.getenv('PS_USER'))

#driver.get("http://fin.bdo.com")
driver.get("https://auth.bdo.com/adfs/ls/idpinitiatedsignon?loginToRp=urn:bdo:peoplesoftfinance&wreply=https://fin.bdo.com/psp/P92FBDO/?cmd=start")

time.sleep(3)
driver.find_element_by_id("i0116").send_keys(os.getenv('PS_USER'))
driver.find_element_by_id("idSIButton9").click()

time.sleep(3)

driver.find_element_by_id("passwordInput").send_keys(os.getenv('PS_PASSWORD'))
driver.find_element_by_id("submitButton").click()

time.sleep(20)

driver.find_element_by_id("idSIButton9").click()

time.sleep(5)

#Navigate to Daily Time Entry page
driver.get("https://fin.bdo.com/psp/P92FBDO_newwin/EMPLOYEE/ERP/s/WEBLIB_TE_NAV.WEBLIB_FUNCTION.FieldFormula.iScript_AddTimeReport?TE.Menu.Var=ADMIN&pslnkid=BDO_EPTE_ADDTIMEREPORT&PERIOD_END_DT=2012-11-01&TIME_SHEET_ID=0004431112&VERSION_NUM=1&PAGE=TE_TIME_LINES%27,%27BDO_EPTE_ADDTIMEREPORT%27)")
time.sleep(3)

#Daily Time Entry page - provide date for time entry
driver.switch_to.frame(0)
entry_date = driver.find_element_by_id("EX_TIME_ADD_VW_PERIOD_END_DT")
entry_date.clear()
entry_date.send_keys("02/05/2020")


driver.find_element_by_id("#ICSearch").click()
time.sleep(2)

state = driver.find_element_by_id("EX_TIME_HDR_STATE")
state.clear()
state.send_keys("VA")

locality = driver.find_element_by_id("EX_TIME_HDR_LOCALITY")
locality.clear()
locality.send_keys("VA9999")

driver.find_element_by_id("EX_ICLIENT_WRK_OK_PB").click()

#Time entry webpage
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("ptifrmtgtframe")

#Add project
project = driver.find_element_by_id("PC_FIELDS_WRK_PROJECT_ID$0")
project.clear()
project.send_keys("0786297")

#add activity code
activity = driver.find_element_by_id("PC_FIELDS_WRK_ACTIVITY_ID$0")
activity.clear()
activity.send_keys("6016-11272")

#add comments
comment = driver.find_element_by_id("EX_TIME_DTL_COMMENTS$0")
comment.clear()
comment.send_keys("test comment")

#add rows
driver.find_element_by_id("EX_TIME_DTL$new$0$$0").click()

#admin time entry
admin = driver.find_element_by_id("POL_TIME1$0")
admin.clear()
admin.send_keys("1.0")

driver.switch_to.frame("vRCPgltAreaFrameDiv")

#admin = POL_TIME1$0
#pto = "POL_TIME1$8"
#holiday = POL_TIME1$5
#busdev = POL_TIME1$7
#training = POL_TIME1$10

#driver.close()