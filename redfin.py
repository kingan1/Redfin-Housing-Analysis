from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os.path
import csv
import json

"""
firefoxProfile = webdriver.FirefoxProfile();
direc = os.getcwd()
firefoxProfile.set_preference("browser.download.panel.shown", False)
firefoxProfile.set_preference("browser.helperApps.neverAsk.openFile","text/csv,application/vnd.ms-excel")
firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel")
firefoxProfile.set_preference("browser.download.folderList", 2);
firefoxProfile.set_preference("browser.download.dir", direc)

driver = webdriver.Firefox(firefoxProfile)
# Open up the Raleigh page
driver.get('http://www.redfin.com/city/35711/NC/Raleigh')
# Click on the "Remove Outline" button to expand our view
driver.find_element_by_class_name("RemoveOutlineButton").click()
time.sleep(5)
zoomOut = driver.find_element_by_class_name("zoomMinusControlButton")
zoomOut.click()
time.sleep(2)
zoomOut.click()
time.sleep(2)
button = driver.find_element_by_id('download-and-save')
link = button.get_attribute('href')
link = link.replace('350', '10000')
time.sleep(1)
driver.execute_script('arguments[0].setAttribute("href", arguments[1]);', button, link)
button.click()
time.sleep(10)
files = os.listdir()
"""
# get the most recent file, which is the downloaded file
filename = max([f for f in os.listdir()], key=os.path.getctime)
print(filename)
# move the file into data
os.rename(filename, f"data/{filename}")
filename = "data/" + filename
print("done")
csvfile = open(filename, "r")
jsonfile = open("data/file.json", "w")
# fieldnames = ('SALE TYPE','SOLD DATE','PROPERTY TYPE','ADDRESS,CITY,STATE OR PROVINCE','ZIP OR POSTAL CODE','PRICE','BEDS','BATHS','LOCATION','SQUARE FEET','LOT SIZE','YEAR BUILT','DAYS ON MARKET','$/SQUARE FEET','HOA/MONTH','STATUS','NEXT OPEN HOUSE START TIME','NEXT OPEN HOUSE END TIME','URL (SEE http://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)','SOURCE','MLS#','FAVORITE','INTERESTED','LATITUDE','LONGITUDE')
reader = csv.DictReader(csvfile)
lst = []
for row in reader:
    lst.append(row)
    json.dump(row, jsonfile)
    jsonfile.write("\n")
json.dump(lst, jsonfile)
jsonfile.close()
