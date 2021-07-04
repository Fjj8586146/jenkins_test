from appium import webdriver
from time import sleep
import pytest
# 定义一个字典
from appium.webdriver.common.touch_action import TouchAction

# desired_caps = dict()
#
# # 平台名字，大小写无所谓
# desired_caps['platformName'] = 'Android'
# # 平台的版本
# desired_caps['platformVersion'] = '7.1.2'
# # 设备的名字，安卓不用，随便写，不能为空;iOS不能乱写
# desired_caps['deviceName'] = 'a'
# # 要打开的应用程序
# desired_caps['appPackage'] = 'com.android.settings'
# # 要打开的界面
# desired_caps['appActivity'] = '.ChooseLockPattern'
# # 默认输入中文无效，但不会报错，需要前置代码中加入下面两个设置
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
# # 连接Appium服务
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.find_element_by_id('com.android.settings:id/search').click()
#
# element = driver.find_element_by_id('android:id/search_src_text')
# print(element.location)
# print(element.size)

# element.send_keys('dfdfdsffdsfsdfsdfsdfsd')
# element.clear()
#
# print('----------------')
# element.send_keys('啊打发实打实大苏打实打实')
# print('-----------------')
from base.read_txt import read_txt

sleep(2)
# driver.find_element_by_xpath('//*[@content-desc="收起"]').click()


# # 定位一组元素
# a = driver.find_elements_by_id('android:id/title')
# print(a)
# # print(len(a))
# for i in a:
#     print(i.get_attribute('enabled'),
#           i.get_attribute('clickable'),
#           i.get_attribute('text'),
#           i.get_attribute('name'),
#           i.get_attribute('resourceId'),
#           i.get_attribute('className'))

# # 滑动一段距离 swipe
# driver.swipe(100, 500, 100, 100, 200)


# scroll 和 drag_and_drop  滑动
# driver.implicitly_wait(3)
# element1 = driver.find_element_by_xpath('//*[@text="WLAN"]')
# element2 = driver.find_element_by_xpath('//*[@text="通知"]')

# driver.scroll(element2, element1)

# 模拟手指轻巧，相当于click（），可以设置轻敲的次数
# TouchAction(driver).tap(element1).perform()

# 模拟手中按下和释放
# TouchAction(driver).press(element1).perform()
# sleep(2)
# TouchAction(driver).press(element1).release().perform()

# 等待操作(组合动作)

# TouchAction(driver).tap(element1).perform()
# sleep(2)
# 长按
# TouchAction(driver).long_press(x=350, y=350, duration=2000).perform()

# 移动
# (TouchAction(driver).press(x=210, y=904)
#  .move_to(x=540, y=904).move_to(x=866, y=904)
#  .move_to(x=866, y=1231).move_to(x=540, y=1231)
#  .move_to(x=210, y=1231).move_to(x=540, y=1560)
#  .perform())

# 获取屏幕分辨率
# a = driver.get_window_size()
# print(a['width'])

# 获取和设置手机网络
# print(driver.network_connection)
# driver.set_network_connection(6)
# print(driver.network_connection)

# 发送按键
# driver.press_keycode(4)
#
# driver.press_keycode(25)
# sleep(1)
# driver.press_keycode(25)
# sleep(1)
# driver.press_keycode(25)
# sleep(1)
#
# driver.press_keycode(24)
# sleep(1)
#
# driver.press_keycode(24)
# sleep(1)
#
# driver.press_keycode(24)
# sleep(2)
# 打开通知栏
# driver.open_notifications()
# # # 手指向上划关闭通知栏
# driver.swipe(100, 1500, 100, 600, 500)

# # 按返回键关闭通知栏
# driver.press_keycode(4)

# 点击屏幕任意地方关闭通知栏
# TouchAction(driver).tap(x=1000, y=1000)
#
# sleep(2)
# driver.quit()

def get_data():
    arr = []
    for i in read_txt('data.txt'):
        arr.append(tuple(i.strip().split(',')))

    return arr[1::]

class TestName:
    # desired_caps = dict()
    # driver = None

    def setup(self):
        pass
        # self.desired_caps = dict()
        #
        # # 平台名字，大小写无所谓
        # self.desired_caps['platformName'] = 'Android'
        # # 平台的版本
        # self.desired_caps['platformVersion'] = '7.1.2'
        # # 设备的名字，安卓不用，随便写，不能为空;iOS不能乱写
        # self.desired_caps['deviceName'] = 'a'
        # # 要打开的应用程序
        # self.desired_caps['appPackage'] = 'com.tencent.mm'
        # # 要打开的界面
        # self.desired_caps['appActivity'] = '.plugin.account.ui.WelcomeActivity'
        # # 默认输入中文无效，但不会报错，需要前置代码中加入下面两个设置
        # self.desired_caps['unicodeKeyboard'] = True
        # self.desired_caps['resetKeyboard'] = True
        # # 连接Appium服务
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def teardown(self):
        # sleep(2)
        # self.driver.quit()
        pass

    @pytest.mark.parametrize(('qqcount', 'password'), get_data())
    def test_name(self, qqcount, password):
        # self.driver.implicitly_wait(20)
        # self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        # self.driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()
        # self.driver.find_element_by_xpath('//*[@content-desc= "请输入QQ号码或手机或邮箱"]').send_keys(qqcount)
        # self.driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys(password)

        # self.driver.find_elements_by_id('com.android.contacts:id/floating_action_button').click()
        # self.driver.find_element_by_id('com.android.settings:id/search').click()
        # self.driver.find_element_by_id('android:id/search_src_text').send_keys(search)

        print(qqcount)
        print(password)
