from base.customCommands import elementPage
import utilities.CustomLogger as cl


class ContactForm(elementPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    contactFromButton = "com.code2lead.kwad:id/ContactUs"  # id
    pagetitle = "Contact Us form"  # text
    nameField = "Enter Name"  # text
    emailField = "Enter Email"  # text
    addressField = "Enter Address"  # text
    mobileNumberField = "4"  # index number
    submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self.contactFromButton, "id")
        cl.allureLogs("Clicked on Contact us Form Button")

    def verifyContactPage(self):
        element = self.isDisplayed(self.pagetitle, "text")
        assert element == True
        cl.allureLogs("Contact Us Form Page open")

    def enterName(self, name):
        self.sendText(name, self.nameField, "text")
        cl.allureLogs("Entered name")

    def enterEmail(self, email):
        self.sendText(email, self.emailField, "text")
        cl.allureLogs("Entered email")

    def enterAddress(self, address):
        self.sendText(address, self.addressField, "text")
        cl.allureLogs("Entered address")

    def enterMNumber(self, phoneNumber):
        self.sendText(phoneNumber, self.mobileNumberField, "index")
        cl.allureLogs("Entered phone numer")

    def clickSubmitButton(self):
        self.clickElement(self.submitButton, "text")