from playwright.sync_api import expect
class loginPage:
    def __init__(self,page):
        self.emailTextBox = page.locator("#ap_email_login")
        self.submitBtn = page.locator('//input[@type="submit"]')
        self.passwordTextBox = page.locator("#ap_password")
        self.emailError = page.locator("#invalid-email-alert")


    def enterEmailID(self,id):
        self.emailTextBox.fill(id)

    def clickOnSubmit(self):
        self.submitBtn.click()

    def enterPassword(self,pw):
        self.passwordTextBox.fill(pw)

    def validateEmailError(self):
        expect(self.emailError).to_be_visible(timeout=10000)