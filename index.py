from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

#获取网页执行机器人
class Daily():
    options = Options()
    options.add_argument('-headless')  # 设置无头
    brower = Firefox(executable_path='/usr/bin/geckodriver', options=options)
    # 连接URL并登录
    brower.get("http://10.x.x.x")
    brower.find_element_by_name("user").send_keys('password')
    brower.find_element_by_name("user").send_keys("password")
    button = brower.find_element_by_class_name("btn")
    button.click()

if __name__ == '__main__':
    Daily()


