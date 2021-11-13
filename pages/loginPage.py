from base.customCommands import elementPage
import utilities.CustomLogger as cl


class LoginPage(elementPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    loginbutton ="com.code2lead.kwad:id/Login" # id
    emailField ="3" # index
    passwordField ="Enter Password" # text
    clickloginButton ="com.code2lead.kwad:id/Btn3" # id
    wrongCredentials = "Wrong Credentials" # text
    pageTitle ="Enter Admin" # text
    textField ="com.code2lead.kwad:id/Edtadmin" # id
    submitButton ="SUBMIT" # text


    def clickLoginBotton(self):
        self.clickElement(self.loginbutton,"id")
        cl.allureLogs("Click on Login Button")

    def enterEmail(self, email):
        self.sendText(email,self.emailField,"index")
        cl.allureLogs("Entered email id")

    def enterPassword(self, password):
        self.sendText(password,self.passwordField,"text")
        cl.allureLogs("Entered Password")

    def enterPassword2(self, password2):
        self.sendText(password2,self.passwordField,"text")
        cl.allureLogs("Entered Password")

    def clickOnLoginB(self):
        self.clickElement(self.clickloginButton,"id")
        cl.allureLogs("Clicked on Login Button in Login Screen")

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self.pageTitle,"text")
        assert adminScreen == True
        cl.allureLogs("Opened Admin Screen")

    def enterText(self, text):
        self.sendText(text,self.textField,"id")
        cl.allureLogs("Entered Text")

    def clickOnSubmit(self):
        self.clickElement(self.submitButton,"text")
        cl.allureLogs("Clicked on Submit Button")
