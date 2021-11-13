from appium import webdriver

class startApp:
    def openApp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel 2'
        desired_caps['app'] = ('/Users/bartoszkuczera/Downloads/Projects/Appium-Python-Selenium-Test-Project/Android_Demo_App.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        return driver