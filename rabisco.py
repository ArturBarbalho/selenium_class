from classes.seleniumWD import WD

#ctr + f na aba de inspecionar elementos permite digitar um seletor para saber se ele é unico

link = 'https://stackoverflow.com/questions/19442562/using-selenium-webdriver-to-obtain-the-active-status-of-an-element' 
driver = WD(link)

search = driver.ByText('Products')
search.click()



