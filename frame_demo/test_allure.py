from time import sleep

import allure
@allure.feature("一级分类")
@allure.story("二级分类")
@allure.title("标题")
@allure.issue("http://ui.yansl.com/#/checkbox","bug")
@allure.testcase("http://ui.yansl.com/#/checkbox","用例")
#生成allure报告，添加断言
def test_report(driver):
    url="http://ui.yansl.com/#/checkbox"
    with allure.step("打开网页{}：".format(url)):pass
    driver.get(url)
    with allure.step("点击多选框：{}".format('//*[@id="form"]/form/div[1]/div/input[1]')):
        allure.attach(driver.get_screenshot_as_png(), '', allure.attachment_type.PNG)
    driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/input[1]').click()
    sleep(2)

