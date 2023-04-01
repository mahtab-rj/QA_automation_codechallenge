class Textbox:
    def __init__(self, driver):
        self.driver = driver
        self.fullName_textbox_id = "userName"
        self.email_textbox_id = "userEmail"
        self.currentAddress_textbox_id = "currentAddress"
        self.permanentAddress_textbox_id = "permanentAddress"
        self.submit_button_id = "submit"

    def enter_fullname(self, fullname):
        self.fullname = fullname
        self.driver.find_element('id', self.fullName_textbox_id).send_keys(fullname)

    def enter_email(self, email):
        self.email = email
        self.driver.find_element('id', self.email_textbox_id).send_keys(email)

    def enter_currentaddress(self, currentaddress):
        self.currenaddress = currentaddress
        self.driver.find_element('id', self.currentAddress_textbox_id).send_keys(currentaddress)

    def enter_permanentaddress(self, permanentaddress):
        self.permanentaddress = permanentaddress
        self.driver.find_element('id', self.permanentAddress_textbox_id).send_keys(permanentaddress)

    def click_on_submit_button(self):
        submit = self.driver.find_element('id', self.submit_button_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

    def verify_checkbox(self):
       fname = self.driver.find_element('xpath', "//*[@class='mb-1' and @id='name']")
       email = self.driver.find_element('xpath', "//*[@class='mb-1' and @id='email']")
       currentAddress = self.driver.find_element('xpath', "//*[@class='mb-1' and @id='currentAddress']")
       permanentAddress = self.driver.find_element('xpath', "//*[@class='mb-1' and @id='permanentAddress']")
       assert fname.text == f'Name:{self.fullname}'
       assert email.text == f'Email:{self.email}'
       assert currentAddress.text == f'Current Address :{self.currenaddress}'
       assert permanentAddress.text == f'Permananet Address :{self.permanentaddress}'
