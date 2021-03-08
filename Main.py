import Login_in
import index
import Image_fenge
import To_word
import Mail_send
import get_for_linux
import schedule
import time
import get_size
class Main():
    def main(self):
        #主页面截图
        print(time.asctime(time.localtime(time.time())))
        get_size.Size.zabbix_main_page("wwp")
        Login_in.Login_in.get_screenshot_main_page("wwp")
        # DNS截图
        get_size.Size.zabbix_DNS("wwp")
        Login_in.Login_in.get_screenshot_DNS1("wwp")
        Login_in.Login_in.get_screenshot_DNS2("wwp")
        #index.Daily.brower.close()
        #对图片操作分割
        Image_fenge.Image_fenge.division("wwp")
        Image_fenge.Image_fenge.lielu("wwp","zabbix3.png")
        Image_fenge.Image_fenge.lielu("wwp","zabbix5.png")
        #从linux上获取数据
        get_for_linux.remote_scp()
        #将数据写入WPS
        To_word.to_wps()
        #发送邮件
        Mail_send.Mail_send()
        print("test结束",time.asctime(time.localtime(time.time())))
if __name__ == '__main__':
     #Main().main()
     #schedule.every(30).minutes.do(Main().main)
     schedule.every().day.at("10:30").do(Main().main)
     while True:
         schedule.run_pending()
         time.sleep(1)


