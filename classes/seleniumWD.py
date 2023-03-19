from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WD(webdriver.Chrome):
    def __init__(self, link, driver_path= r"C:/Selenium Driver"):
        self.link = link
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver_path = driver_path
        super(WD, self).__init__(options=options)
        self.implicitly_wait(5)
        self.get(self.link) 
        self.Keys = Keys

    def ByCssSelector(self, selector):
        element = self.find_element(By.CSS_SELECTOR, selector) 
        return element
    
    def ById(self, Id):
        element = self.find_element(By.ID, Id) 
        return element
    
    def ByClass(self, Class):
        element = self.find_element(By.CLASS_NAME, Class) 
        return element