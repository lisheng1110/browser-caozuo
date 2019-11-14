from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 定义了变量EC表示expected_conditions

from selenium import webdriver


def test_frame(driver):
        driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")
        sleep(2)
        frame = driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
        driver.switch_to.frame(frame)
        sleep(2)
        driver.find_element_by_partial_link_text('京东').click()
        sleep(2)
        driver.switch_to.parent_frame()  # 退出当前ifame
        sleep(2)
        iframe = driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')  # 进入frome
        driver.switch_to.frame(iframe)  # 切换frame
        sleep(2)  # 响应时间
        inpu = driver.find_element_by_xpath('//*[@id="key"]')  # 定位输入框
        inpu.clear()  # 清空
        inpu.send_keys('手机')  # 输入内容
        sleep(2)
        #driver.switch_to.default_content() # 切换到原始页面

def test_wait(driver):#隐式等待
    driver.get("http://ui.yansl.com/#/loading")
    bt = driver.find_element_by_xpath("//span[contains(text(),'指令方式')]")
    bt.click()
    WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located([By.XPATH, '//tbody/tr[1]/td[2]/div'])
    )
    bg = driver.find_element_by_xpath('//tbody/tr[1]/td[2]/div')
    print(bg.text)
    sleep(2)
