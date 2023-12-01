from selenium.webdriver.common.by import By

class Helper():
    def get_text_from_elmts(driver,xp):
        web_elmts = driver.find_elements(By.XPATH,xp)
        web_elmts_txt = [i.get_attribute("textContent") for i in web_elmts]
        return web_elmts_txt