from time import sleep


def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    #下面的要用elements
    button=driver.find_elements_by_xpath("//label[contains(text(),'自动关闭提示')]/..//div/button/span[text()='消息']")
    button[0].click()
    messge=driver.find_element_by_xpath("//div[@role='alert']/p")
    text=messge.text
    print(text)
    assert "这是一条消息" in text#展示文本做断言
    sleep(2)

def test_page_sourcs(driver):
    driver.get("http://ui.yansl.com/")
    driver.find_element_by_xpath("//div[contains(text(),'通知提示')]").click()
    #sleep(2)
    driver.find_element_by_xpath("//li[contains(text(),'消息提示')]").click()
    #sleep(2)
    sourcs=driver.page_source#获取页面源代码
    print(sourcs)
    assert "手工关闭提示" in sourcs
    sleep(2)
