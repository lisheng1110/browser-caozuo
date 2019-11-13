from time import sleep
from selenium import webdriver

driver=webdriver.Chrome("../chrome-driver_v78/chromedriver.exe")#使用Chrome驱动打开浏览器
sleep(1)
driver.maximize_window()#窗口最大化
driver.get("https://www.baidu.com/")#打开百度浏览器，get后面跟浏览器的IP
sleep(1)
driver.get("https://www.jd.com/")
sleep(1)
driver.back()#后退
sleep(1)
driver.forward()#前进
sleep(1)
driver.refresh()#刷新
sleep(1)
driver.quit()#关闭浏览器，并退出driver
