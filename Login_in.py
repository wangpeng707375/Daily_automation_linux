import index
import Full_screenshot
import time

#登录
class Login_in():
    url_1 = 'http://x.x.x.x.'
    "这里写url1_1-url12的URL"
    url_12 = ''



    def get_urlx(self):
        URL_catalogs = {Login_in.url_4: '图片的名称', Login_in.url_5: 'xxx',
                        Login_in.url_7: 'xx', Login_in.url_9: 'xxx'}
        return URL_catalogs

    def get_urly(self):
        URL_catalogs2 = {Login_in.url_2: 'xxx', Login_in.url_3: '',
                         Login_in.url_11: 'xxx', Login_in.url_10: '',
                         Login_in.url_12: ''}
        return URL_catalogs2

    # 登录URL并且截图
    def get_screenshot_main_page(self):
        index.Daily.brower.get(Login_in.url_1)
        time.sleep(20)
        Full_screenshot.Full_screenshot.screenshot1("wwp")

    def get_screenshot_DNS1(self):
        for s_url, catalog in Login_in.get_urlx(1).items():
            index.Daily.brower.get(s_url)
            time.sleep(10)
            Full_screenshot.Full_screenshot.screenshot2("wwp", catalog)

    def get_screenshot_DNS2(self):
        for s_url, catalog in Login_in.get_urly(1).items():
            index.Daily.brower.get(s_url)
            time.sleep(150)
            Full_screenshot.Full_screenshot.screenshot2("wwp", catalog)


if __name__ == '__main__':
    pass


