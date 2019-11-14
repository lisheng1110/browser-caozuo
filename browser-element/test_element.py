from time import sleep

import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_inputs(driver):#对纯输入框操作
    driver.get("http://ui.yansl.com/#/input")#打开网页
    sleep(2)
    inputs=driver.find_element_by_xpath("//input[@name='t1']")#用xpath定位输入框位置
    inputs.clear()#清空输入框内容
    inputs.send_keys("八荒六合君为尊，万水千山我是王")#send_keys()输入内容
    sleep(2)

def test_redio(driver):#对单选框操作
    driver.get("http://ui.yansl.com/#/radio")#打开网页
    sleep(2)
    radio=driver.find_element_by_xpath("//input[@name='sex'][2]")#使用xpath定位“性别女”元素
    radio.click()#点击
    sleep(2)
def test_checkbox(driver):#对多选框操作
    driver.get("http://ui.yansl.com/#/checkbox")#打开网页
    checkbox=driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/label[1]/span[1]/span")#使用xpath定位
    sleep(1)
    checkbox.click()
    sleep(2)
def test_select(driver):#对下拉框选择操作
    driver.get("http://ui.yansl.com/#/select")#打开网页
    sleep(1)
    select = driver.find_element_by_xpath("//input[@name='item2']")#使用xpath定位元素位置
    select.click()
    sleep(2)
    options=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[5]/span")#使用xpath定位元素位置
    actions=ActionChains(driver)#ActionChains对鼠标键盘操作，需要导包
    actions.move_to_element(options).perform()#移动鼠标到选定位置执行
    sleep(2)
    options.click()
    sleep(2)

def test_time(driver):#对任意时间输入框操作
    driver.get("http://ui.yansl.com/#/dateTime")#打开网页
    sleep(1)
    t=driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[2]/div/div/input")#使用xpath定位元素位置
    sleep(1)
    t.click()
    t.send_keys("06:06:06")#任意时间可以直接输入时间
    sleep(2)
def test_file1(driver):#对上传文件图片操作
    driver.get("http://ui.yansl.com/#/upload")#打开网页
    sleep(1)
    file=driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")#使用xpath定位元素位置
    file.clear()#清空内容
    file.send_keys("c:\\Users\\guoya\\Desktop\\微信图片_20191113144935.png")#输入文件的路径，单斜杠要换成双的
    sleep(2)

def test_file2(driver):#上传图片，非浏览器内部操作,需要pip install pyautoit-win64
    driver.get("http://ui.yansl.com/#/upload")#打开网页
    sleep(1)
    file=driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button/span")#使用xpath定位元素位置
    file.click()
    #下面的代码是固定格式，只需要修改文件路径即可，ps：autoit需要导包
    autoit.win_wait("打开", 10)
    sleep(1)
    #   autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "c:\\Users\\guoya\\Desktop\\微信图片_20191113144935.png")
    sleep(3)
    autoit.control_click("打开", "Button1")
    sleep(2)

def test_alert(driver):#对弹框操作
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")#打开网页
    sleep(1)
    button=driver.find_element_by_xpath("/html/body/table/tbody/tr[6]/td[2]/input")#使用xpath定位元素位置
    button.click()
    sleep(2)
    alert=driver.switch_to.alert#切换弹窗的关键字switch_to.alert
    alert.send_keys("hello,world")
    alert.accept()#弹窗确认accept，弹窗取消dismiss
    sleep(2)
def test_windows(driver):#Windows窗口切换操作
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")#打开网页
    sleep(2)
    dang_dang = driver.find_element_by_link_text("当当")#使用超链接文本定位，输入文本关键字
    actions = ActionChains(driver)#启用键盘和鼠标，需要导包
    #按下key_down（Keys.这里放按键ps：control）；松开key_up（Keys.这里放松开的按键ps：control）
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)#启用键盘和鼠标，需要导包
    # 按下key_down（Keys.这里放按键ps：control）；松开key_up（Keys.这里放松开的按键ps：control）
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")#根据文本链接模糊关键字定位
    actions = ActionChains(driver)#启用键盘和鼠标，需要导包
    # 按下key_down（Keys.这里放按键ps：control）；松开key_up（Keys.这里放松开的按键ps：control）
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)
    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)#循环切换窗口
        sleep(2)
        if driver.title.__contains__("京东"):#判断含有“京东”关键字标题的窗口
            break
