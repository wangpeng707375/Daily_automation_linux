from PIL import Image
import os
class Image_fenge():
    # 对zabbix主页面.png分割
    def division(self):
        filename = r'/usr/local/python_on/Daily_automation_linux/Daily_picture/zabbix主页面.png'
        img = Image.open(filename)
        # 监控标题
        box = (50, 50, 1900, 200)
        region = img.crop(box)
        region.save('/usr/local/python_on/Daily_automation_linux/Daily_picture/zabbix1.png')

        # 监控设备状态
        box = (50, 200, 2144, 1000)
        region = img.crop(box)
        region.save('/usr/local/python_on/Daily_automation_linux/Daily_picture/zabbix2.png')

        # 监控链路1*6
        box = (70, 1310, 2144, 2230)
        region = img.crop(box)
        region.save('/usr/local/python_on/Daily_automation_linux/Daily_picture/zabbix3.png')

        # 监控链路2*2
        box = (70, 2240, 1100, 2640)
        region = img.crop(box)
        region.save('/usr/local/python_on/Daily_automation_linux/Daily_picture/zabbix4.1.png')
        box = (1100, 2240, 2130, 2640)
        region = img.crop(box)
        region.save('/usr/local/python_on/Daily_automation_linux/Daily_picture/zabbix4.2.png')

        # 监控链路3*6
        box = (70, 2650, 2144, 3550)
        region = img.crop(box)
        region.save('/usr/local/python_on/Daily_automation_linux/Daily_picture/zabbix5.png')

    # 批量分割截图
    def lielu(self, zabbix):
        list_Before = r'/usr/local/python_on/Daily_automation_linux/Daily_picture'
        filename = os.path.join(list_Before, zabbix)
        img = Image.open(filename)
        size = img.size
        weight = int(size[0] // 2)
        height = int(size[1] // 3)
        # 切割后的小图的宽度和高度
        for j in range(3):
            for i in range(2):
                box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
                region = img.crop(box)
                region.save('/usr/local/python_on/Daily_automation_linux/Daily_picture/{}{}_{}'.format(i, j, zabbix))

    def DNS_fengge(self,wp_png,catalog):
        catalog_left =r'/usr/local/python_on/Daily_automation_linux/Daily_picture'
        picture_name = os.path.join(catalog_left, catalog)
        catalog_TOP10=catalog+"_VS_TOP10连接数.png"
        picture_name_TOP10=os.path.join(catalog_left,catalog_TOP10)
        img=Image.open(wp_png)
        box = (70,110, 2000, 940)
        region = img.crop(box)
        region.save(picture_name)
        box = (70, 950, 2000, 1530)
        region = img.crop(box)
        region.save(picture_name_TOP10)


if __name__ == '__main__':
    Image_fenge.division(1)
    a = "zabbix3.png"
    b = "zabbix5.png"
    Image_fenge.lielu(1,a)
    Image_fenge.lielu(1,b)
