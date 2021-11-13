from threading import local
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import utilities.CustomLogger as cl
import time


class elementPage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def findElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(
                lambda x: x.find_element_by_class_name(locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator(
                'text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(
                lambda x: x.find_element_by_xpath('%s' % (locatorvalue)))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.findElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " +
                          locatorType + " with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.findElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        return element

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
            return True
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            self.takeScreenshot(locatorType)
            return False

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + \
            (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "/Users/bartoszkuczera/Downloads/Projects/Appium-Python-Selenium-Test-Project/screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info(
                "Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=text, attachment_type=AttachmentType.PNG)

    def swipe(self, Xstart, Ystart, Xend, Yend):
        time.sleep(1)
        TouchAction(self.driver).long_press(x=Xstart, y=Ystart).move_to(
            x=Xend, y=Yend).release().perform()

    def dragAnddropByCoordinates(self, Xdrag, Ydrag, Xdrop, Ydrop):
        try:
            TouchAction(self.driver).long_press(x=Xdrag, y=Ydrag).move_to(
                x=Xdrop, y=Ydrop).release().perform()
        except:
            "cannot drag and drop by coordinates"

    def dragAndDropByElements(self, selector1, selector2, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            locator1 = self.findElement(selector1, locatorType)
            locator2 = self.findElement(selector2, locatorType)
            TouchAction(self.driver).long_press(locator1).move_to(
                locator2).release().perform()
        except:
            self.log.info(
                "Unable to drag and drop")
        return element

    def keyCodes(self, value):
        try:
            self.driver.press_keycode(value)
        except:
            self.log.info("cannot use key code")
