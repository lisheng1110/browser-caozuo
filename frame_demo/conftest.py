from time import sleep
import pytest
from selenium import webdriver
#启用fixture函数 把公共信息放在方法driver中，在其他模块中方法参数中引用
@pytest.fixture(scope="session")
def driver():
    driver=webdriver.Chrome("../chrome-driver_v78/chromedriver.exe")#使用Chrome驱动打开浏览器
    sleep(1)
    driver.maximize_window()#窗口最大化
    driver.implicitly_wait(10)  # 设置隐形等待
    sleep(1)
    yield driver
    driver.quit()

