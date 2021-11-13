import unittest
import pytest
import utilities.CustomLogger as cl
from base.customCommands import elementPage
from pages.loginPage import LoginPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class loginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lt = LoginPage(self.driver)
        self.bp = elementPage(self.driver)

    @pytest.mark.run(order=1)
    def test_loginFailMethod(self):
        cl.allureLogs("App Opened")
        self.lt.clickLoginBotton()
        self.lt.enterEmail("ashton@gmail.com")
        self.lt.enterPassword2("1234")
        self.lt.clickOnLoginB()
        self.lt.verifyAdminScreen()

    @pytest.mark.run(order=2)
    def test_openLoginScreen(self):
        self.bp.keyCodes(4)
        self.lt.clickLoginBotton()
        self.lt.enterEmail("admin@gmail.com")
        self.lt.enterPassword("admin123")
        self.lt.clickOnLoginB()
        self.lt.verifyAdminScreen()

    @pytest.mark.run(order=3)
    def test_enterDataInEditBox(self):
        self.lt.enterText("Code2Lead")
        self.lt.clickOnSubmit()
