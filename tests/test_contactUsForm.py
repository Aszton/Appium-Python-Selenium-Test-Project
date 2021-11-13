import unittest
import pytest
from pages.contactUsFormPage import ContactForm
import utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class contactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run()
    def test_openContactFormAndEnterData(self):
        cl.allureLogs("App Launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
        self.cf.enterName("Ashton")
        self.cf.enterEmail("ashton@gmail.com")
        self.cf.enterAddress("gdanska 25")
        self.cf.enterMNumber("444555666")
        self.cf.clickSubmitButton()