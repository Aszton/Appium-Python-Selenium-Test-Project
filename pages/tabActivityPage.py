import time
from base.customCommands import elementPage
import utilities.CustomLogger as cl


class tabActivityPage(elementPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    tabActivityButton ="com.code2lead.kwad:id/TabView" # id

    def clickTabActivityButton(self):
        self.clickElement(self.tabActivityButton,"id")
        cl.allureLogs("Click on Tab Activity Button")

    def swipeFromLeftToRight(self):
        self.swipe(1000,1005,192,992)

    def swipeFromRightToLeft(self):
        self.swipe(100,1000,1000,1000)