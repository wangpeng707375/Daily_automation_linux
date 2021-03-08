import index
import Image_fenge
#全屏截图
class Full_screenshot():
    #全屏截图（zabbix主界面）
    def screenshot1(self):
        index.Daily.brower.get_screenshot_as_file('/usr/local/python_on/Daily_automation_linux/Daily_picture/zabbix主页面.png')
    #全屏截图(DNS)
    def screenshot2(self,catalog):
        index.Daily.brower.get_screenshot_as_file('/usr/local/python_on/Daily_automation_linux/Daily_picture/wp.png')
        Image_fenge.Image_fenge.DNS_fengge('wwp','/usr/local/python_on/Daily_automation_linux/Daily_picture/wp.png',catalog)
if __name__ == '__main__':
    pass
    # for  catalog in Login_in.Login_in.get_urlx(1).items():
    #     Full_screenshot.screenshot2("wwp", catalog)
