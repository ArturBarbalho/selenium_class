from classes.seleniumWD import WD

link = 'https://www.seleniumeasy.com' 
driver = WD(link)

search = driver.ByCssSelector("input[placeholder='Search']")
search.click()
search.send_keys('Java')
search.send_keys(driver.Keys.ENTER)

driver.quit()