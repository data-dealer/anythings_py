# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:46:58 2018

@author: User
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

driver = webdriver.Chrome()
driver.get('http://online.buh.edu.vn/')
#for i in range(10):

#    driver.refresh()


dangnhap = driver.find_element_by_id('lbtDangnhap')
dangnhap.click()

#username = Select(driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_txtUserName'))
#-----------Login
driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_txtUserName').send_keys('030630140646')
driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_txtPassword').send_keys('emlaminhnha123')
#driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_cbRemember').checked()
driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_btLogin').click()
#
#--------------------dang ky hoc phan
driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_lnkDangKy').click()

driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_ctl00_btSubmit').click() # dang ký học phàn




  

driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_lnkDangkyxettotnghiep').click()
driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_ctl00_btnInbangdiem').click()

driver.find_element_by_id('pnlPrint')

driver.get('http://online.buh.edu.vn/Portlets/uis_Myspace/Student/Graduations/GraduationMarks.aspx?Studentid=030630140646&StudyProgramID=K30DH405_2')

try :
    driver.find_element_by_id('lbtDangnhap')
except NoSuchElementException:
    while True:
        driver.refresh()
        print('Co loi xay ra!')  
   
lista = driver.find_element_by_xpath("//td[@class ='studyprogram_tabledetails_td_content_aligncenter_dl']")

links_dk = driver.find_elements_by_xpath("//img[@title ='Nhấn vô đây để đăng ký lớp học phần.']")

list_links =[]
for link in links_dk:
    str_img = link.get_attribute('onclick').split("'")[1]
    list_links.append(str_img)


dslop = driver.find_elements_by_xpath("//td[@class ='studyprogram_tabledetails_td_content_bottom_left_dl']")
dstenlop = []
for name in dslop:
    dstenlop.append(name.text.strip().upper())


from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome()
browser.get('http://online.buh.edu.vn/')
first_result = ui.WebDriverWait(browser, 15).until(lambda browser: browser.find_element_by_class_name('rc'))
first_link = first_result.find_element_by_tag_name('a')


i = 0 
notfind = True
while notfind :
    i += 1
    browser.find_element_by_id('lbtDangnhap').click()
    #username = Select(driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_txtUserName'))
    #-----------Login
    browser.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_txtUserName').send_keys('030630140646')
    browser.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_txtPassword').send_keys('emlaminhnha123')
    #driver.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_cbRemember').checked()
    browser.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_btLogin').click()
    #
    #--------------------dang ky hoc phan
    browser.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_lnkDangKy').click()
    
    browser.find_element_by_id('ContentPlaceHolder1_ctl00_ctl00_ctl00_btSubmit').click() # dang ký học phàn

    try:
        element = WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ctl00_ctl00_lnkDangKy2"))
        )
        
    except:
        browser.refresh()
        print(i)
        continue
    element.click()
    notfind = False

# Save the window opener (current window, do not mistaken with tab... not the same)
main_window = browser.current_window_handle
# Open the link in a new tab by sending key strokes on the element
# Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack 
first_link.send_keys(Keys.CONTROL + Keys.RETURN)

# Switch tab to the new tab, which we will assume is the next one on the right
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    
# Put focus on current window which will, in fact, put focus on the current visible tab
browser.switch_to_window(main_window)

# do whatever you have to do on this page, we will just got to sleep for now
sleep(2)

# Close current tab
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

# Put focus on current window which will be the window opener
browser.switch_to_window(main_window)
