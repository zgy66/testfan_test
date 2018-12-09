from selenium import webdriver
from time import sleep
import random

url = "http://39.98.63.132:8040/"

dr = webdriver.Ie()
dr.get(url)

#登录
dr.find_element_by_css_selector('#username').clear()
dr.find_element_by_css_selector('#username').send_keys("admin")
dr.find_element_by_css_selector('#password').clear()
dr.find_element_by_css_selector('#password').send_keys("admin")
dr.find_element_by_css_selector('#add-code').clear()
dr.find_element_by_css_selector('#add-code').send_keys("1111")
dr.find_element_by_css_selector('#imageField').click()
sleep(3)
#人员维护
dr.switch_to.frame(1)
dr.find_element_by_name("ri2").click()
#查询
dr.switch_to.default_content()   #还原之前定位
dr.switch_to.frame("main")
# dr.switch_to.frame(3)
dr.find_element_by_name("select-key:useruuid").send_keys("zhangsan8421")
dr.find_element_by_name("select-key_submit").click()
sleep(2)
#新增
dr.find_element_by_class_name("grid-menu").click()
# signal = False
# for i in range(10):
#     windowsHandlers = dr.window_handles
#     for h in windowsHandlers:
#         dr.switch_to.window(h)
#         title = dr.title
#         if "增加人员维护" == title:
#             signal = True
#             break
#     if signal: break
handles = dr.window_handles
for handle in handles:
    if dr.current_window_handle == handle:
        break
    else:
        dr.switch_to.window(handle)
        break
username = str(random.randint(666,777))
dr.find_element_by_name("record:useruuid").send_keys("Zgy"+ username)
dr.find_element_by_name("record:name").send_keys("郑杰")
dr.find_element_by_name("record:department").send_keys("管理部门")
a = dr.find_element_by_name("record:roleuuid")
a.find_element_by_xpath("//option[@value='项目管理办公室']").click()
b = dr.find_element_by_name("record:ability")
b.find_element_by_xpath("//option[@value='000004']").click()
dr.find_element_by_name("record_record_saveAndExit").click()
sleep(3)
#第二次查询
# signal = False
# for i in range(10):
#     windowsHandlers = dr.window_handles
#     for h in windowsHandlers:
#         dr.switch_to.window(h)
#         title = dr.title
#         if "软件应用框架" == title:
#             signal = True
#             break
#     if signal: break
# dr.switch_to.default_content()  #还原之前定位
# dr.switch_to.frame(1)
# dr.find_element_by_name("ri2").click()
# dr.switch_to.default_content()
dr.switch_to.frame("main")
# dr.switch_to.frame(3)
dr.find_element_by_name('select-key:useruuid').clear()
dr.find_element_by_name("select-key:useruuid").send_keys("Zgy"+ username)
dr.find_element_by_name("select-key_submit").click()
sleep(3)
# 选中新增用户
dr.find_element_by_name("record:_flag").click()
dr.find_element_by_name("record_record_deleteRecord").click()
sleep(3)
dr.switch_to.alert.accept()
sleep(3)
dr.switch_to.alert.accept()
sleep(3)
dr.quit()