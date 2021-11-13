import unittest
import pytest
import utilities.CustomLogger as cl
from base.customCommands import elementPage
from pages.tabActivityPage import tabActivityPage

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class tabActivityTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ta = tabActivityPage(self.driver)

    @pytest.mark.run()
    def test_tabActivity(self):
        cl.allureLogs("App Opened")
        self.ta.clickTabActivityButton()
        self.ta.swipeFromLeftToRight()
        self.ta.swipeFromLeftToRight()
        self.ta.swipeFromRightToLeft()
        self.ta.swipeFromRightToLeft()
