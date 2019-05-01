from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Temp\chromedriver.exe')

driver.get('http://192.168.99.100:5000/')

pageText = driver.find_element_by_xpath('/html/body').text 

print(pageText)