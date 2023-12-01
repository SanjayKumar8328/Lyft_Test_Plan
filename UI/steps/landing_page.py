from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import mainpage_xp as xp
from PageHelpers import Helper as HP

# @after()
# def take_screenshot(self):
#     self.driver.save_screenshot("error_screenshot.png")

@given('Browser for the testing')
def open_browser(self):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    self.driver = driver

@when('open the lyft URL')
def open_url(self):
    self.driver.get("https://www.lyft.com/rider")

@then('Verify the landing page is working fine')
def verify_landing(self):
    time.sleep(3) #implicit waiting
    
    WebDriverWait(self.driver, 8).until(
        EC.presence_of_element_located((By.XPATH, xp.Lpage_wait_xp))
    ) # explicit waiting for 8 sec

@then('Verify all the modes of transportations are availale for the riders')
def modes_available(self):
    expected_modes = ["Wait & Save","Lyft","Bikes & Scooters","Priority Pickup","Extra Comfort","XL","Transit"]
    modes_text = HP.get_text_from_elmts(self.driver,xp.tmode_xp)
    print("TEXT expected is",expected_modes)
    print("TEXT FROM THE PAGE IS",modes_text)
    if len(modes_text) != 7 or modes_text!=expected_modes:
        self.driver.save_screenshot("error_screenshot.png")
        raise AssertionError("expected modes of transport {} are not matching with home page transports {}".format(expected_modes,modes_text))
    
@when("Click on the '{cab_type}' cabs check the mobile number page")
def select_cab(self,cab_type):
    selected_cab = xp.cabs_xp.format(cab_type)
    self.driver.find_element(By.XPATH,selected_cab).click()
    time.sleep(2)
    self.driver.find_element(By.XPATH,xp.book_ride_xp).click()
    time.sleep(3)

@then('validate the redirected page')
def verify_redirection_url(self):
    current_url = self.driver.current_url
    if "ride-with-lyft" not in current_url:
        print("current_url is ",current_url)
        raise AssertionError("After selecting the cab, Book a ride is not redirecting to sign page.")
        