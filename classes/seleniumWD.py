from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WD(webdriver.Chrome):
    def __init__(self, link, hide = False ): 
        options = Options()
        options.add_experimental_option("detach", True)
        if(hide):
            options.add_argument('--headless')
        super(WD, self).__init__(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.set_window_size(1400,1000)
        self.implicitly_wait(5)
        self.get(link) 
        self.Keys = Keys
        self.By = By

    def ByCssSelector(self, selector):
        element = self.find_element(By.CSS_SELECTOR, selector) 
        return element
    
    def ById(self, Id):
        element = self.find_element(By.ID, Id) 
        return element
    
    def ByClass(self, Class):
        element = self.find_element(By.CLASS_NAME, Class) 
        return element
    
    def ByXPATH(self, selector):
        element = self.find_element(By.XPATH, selector) 
        return element
    
    def ByText(self, text):
        element = self.find_element(By.XPATH, f"//*[contains(text(),'{text}')]" ) 
        return element