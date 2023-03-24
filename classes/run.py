from classes.seleniumWD import WD
from datetime import datetime
import os
import sys

class Run:
    def __init__(self):
        self.link = 'https://www.seleniumeasy.com' 
        #app_path = os.path.dirname(sys.executable)                         #produçao
        app_path = R'C:\Users\arthu\Desktop\Programação\Python\exe_testing' #dev
        name = 'test.txt'
        self.final_path = os.path.join(app_path,name)

    def start(self):
        driver = WD(self.link,True)
        search = driver.ByCssSelector("h2[class='slogan']")
        text = search.text

        file = open(self.final_path,'a')
        file.write(f'\n{text}')
        file.close()
        driver.quit()
    
        