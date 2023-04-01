from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime
from time import sleep
import unittest
from TextBox import Textbox
from selenium.webdriver.chrome.service import Service
import HtmlTestRunner

currentDay = datetime.date.today()
formattedDay = datetime.date.strftime(currentDay, "%m/%d/%Y")


class TextBoxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver_service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.driver_service)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_enter_data(self):
        self.driver.get("https://demoqa.com/")
        textbox = Textbox(self.driver)
        elements = self.driver.find_element('xpath', "//*[text()='Elements']")
        self.driver.execute_script("arguments[0].scrollIntoView();", elements)
        sleep(2)
        elements.click()
        self.driver.find_element('xpath', "//*[text()='Text Box']").click()
        textbox.enter_fullname("John Doe")
        textbox.enter_email("johndoe@test.com")
        currentaddress = textbox.enter_currentaddress(formattedDay)
        textbox.enter_permanentaddress("1234567890")
        sleep(2)
        textbox.click_on_submit_button()
        textbox.verify_checkbox()
        sleep(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))