# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:27:50 2018

@author: User
"""

import requests
import lxml.html as lh
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

url='http://s.cafef.vn/bao-cao-tai-chinh/ABC/BSheet/2018/0/0/1/0/bao-cao-tai-chinh-cong-ty-co-phan-truyen-thong-vmg.chn'

#Create a handle, page, to handle the contents of the website
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() 

driver.get(url)

# run
start_time = time.time()
cks = ['hng', 'hsg']
loadcafe(cks,driver)
end_time = round((time.time() - start_time)/60,2)
print("TOTAL_TIME--- %s Minute ---" %end_time,'all complete') 



def loadcafe(cks,driver, outcd , outhd, outlctt):
    for ck in cks:
        ppTrucT = False
        # ghi ten ma chứng khoan
        ma_ck = driver.find_element_by_xpath("//input[@name='txtKeyword']")
        ma_ck.clear()
        ma_ck.send_keys(ck)
        # tim ma chung khoan
        driver.find_element_by_xpath("//img[@id='btSearch']").click()
        # chọn kỳ theo nam
        driver.find_element_by_xpath("//input[@id='rdo0']").click()
        # truoc = driver.find_element_by_xpath("//img[@alt='Xem dữ liệu trước']")  
        # sau = driver.find_element_by_xpath("//img[@alt='Xem dữ liệu tiếp']")
        # cac muc bao cao
    
        #----------KẾT QUẢ KINH DOANH
        driver.find_element_by_xpath("//a[@id='aNhom2']").click()
        kqkd_0 = find_table(driver)
        
        #----------LƯU CHUYỂN TIỀN TỆ GIÁN TIẾP
        driver.find_element_by_xpath("//a[@id='aNhom3']").click()
        lctt_gt_0 = find_table(driver)
        
        if np.isnan(lctt_gt_0[lctt_gt_0.columns[4]][1]):
            ppTrucT = True
        
        #----------LƯU CHUYỂN TIỀN TỆ TRỰC TIẾP
        if ppTrucT :
            driver.find_element_by_xpath("//a[@id='aNhom4']").click()
            lctt_tt_0 = find_table(driver)
        
        #----------CÂN ĐỐI KẾ TOÁN
        driver.find_element_by_xpath("//a[@id='aNhom1']").click() # chon cdkt truoc
        driver.find_element_by_link_text('Mở rộng').click()
        cdkt_0 = find_table(driver)
        #---------------------------------------------------------------
        lable_cdkt = cdkt_0.ix[:, 0:1] # nhan cho cac teu chi
        re_cdkt = cdkt_0.ix[:, 1:5] # lay noi dung cac nam
        
        lable_kqkd = kqkd_0.ix[:, 0:1] # nhan cho cac teu chi
        re_kqkd = kqkd_0.ix[:, 1:5] # lay noi dung cac nam
            
        lable_lctt_gt = lctt_gt_0.ix[:, 0:1] # nhan cho cac teu chi
        re_lctt_gt = lctt_gt_0.ix[:, 1:5] # lay noi dung cac nam
        if ppTrucT :
            lable_lctt_tt = lctt_tt_0.ix[:, 0:1] # nhan cho cac teu chi
            re_lctt_tt = lctt_tt_0.ix[:, 1:5] # lay noi dung cac nam
            
        
        conti = True
        count = 0
        while conti :
            for i in range(4):
                driver.find_element_by_xpath("//img[@alt='Xem dữ liệu trước']").click()
            count +=4
            # cdkt
            driver.find_element_by_xpath("//a[@id='aNhom1']").click()
            new_cdkt = find_table(driver)
            new_cdkt = new_cdkt.ix[:, 1:5]
            re_cdkt = pd.concat([ new_cdkt,re_cdkt], axis=1, sort=False)
            # kqkd
            driver.find_element_by_xpath("//a[@id='aNhom2']").click()
            new_khkd = find_table(driver)
            new_khkd= new_khkd.ix[:, 1:5]
            re_kqkd = pd.concat([ new_cdkt,re_kqkd], axis=1, sort=False)
            # lctt_gt
            driver.find_element_by_xpath("//a[@id='aNhom3']").click()
            new_lctt_gt = find_table(driver)
            new_lctt_gt= new_lctt_gt.ix[:, 1:5]
            re_lctt_gt = pd.concat([ new_cdkt,re_lctt_gt], axis=1, sort=False)
            
            # lctt_tt
            if ppTrucT :
                driver.find_element_by_xpath("//a[@id='aNhom4']").click()
                new_lctt_1t = find_table(driver)
                new_lctt_tt= new_lctt_gt.ix[:, 1:5]
                re_lctt_tt = pd.concat([ new_cdkt,re_lctt_tt], axis=1, sort=False)
            
            if np.isnan(new_cdkt[new_cdkt.columns[1]][0]):
                conti = False
                
        re_cdkt = pd.concat([ lable_cdkt,re_cdkt], axis=1, sort=False)  
        re_kqkd = pd.concat([ lable_kqkd,re_kqkd], axis=1, sort=False)
        re_lctt_gt = pd.concat([ lable_lctt_gt,re_lctt_gt], axis=1, sort=False)
        if ppTrucT :
            re_lctt_tt = pd.concat([ lable_lctt_tt,re_lctt_tt], axis=1, sort=False)
        
        
        re_cdkt.to_csv(ck +"cdkt.csv",index = False)
        re_kqkd.to_csv(ck +"kqkd.csv",index = False)    
        re_lctt_gt.to_csv(ck +"lctt_gt.csv",index = False)
        if ppTrucT :
            re_lctt_tt.to_csv(ck +"lctt_tt.csv",index = False)    
        for cl in range(count):
            driver.find_element_by_xpath("//img[@alt='Xem dữ liệu tiếp']").click()
        
#------------------------------------------------------------------------------------    


    
def find_table(driver):    
    table = driver.find_element_by_id("tableContent").get_attribute('outerHTML')
    col_year = ["tiêu chí"]
    years = driver.find_elements_by_class_name("h_t")
    for y in years:
        col_year.append((y.text))
    df  = pd.read_html(str(table))
    tb1 = df[0]
    tb1 = tb1.dropna(subset =[ 0])
    tb1= tb1.ix[:, 0:4]
    tb1.columns = col_year
    tb1 =tb1.reset_index(drop=True)
    return tb1

