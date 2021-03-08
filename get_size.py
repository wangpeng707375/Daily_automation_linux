import index
class Size():
    def zabbix_main_page(self):
        index.Daily.brower.set_window_size(2144,3700)
        # quan全屏显示 # index.Daily.brower.maximize_window()
        # width = index.Daily.brower.execute_script("return document.documentElement.scrollWidth")
        # height = index.Daily.brower.execute_script("return document.documentElement.scrollHeight")
    def zabbix_DNS(self):
        index.Daily.brower.set_window_size(2000,1700)

if __name__ == '__main__':
    pass
