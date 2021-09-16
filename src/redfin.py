import os.path
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox import options


def run():
    # Initializing firefox browser
    # Have to configure how files are saved
    firefoxProfile = webdriver.FirefoxProfile()
    opt = options.Options()
    opt.headless = True
    direc = os.getcwd()
    firefoxProfile.set_preference("browser.download.panel.shown", False)
    firefoxProfile.set_preference(
        "browser.helperApps.neverAsk.openFile", "text/csv,application/vnd.ms-excel"
    )
    firefoxProfile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel"
    )
    firefoxProfile.set_preference("browser.download.folderList", 2)
    firefoxProfile.set_preference("browser.download.dir", direc)
    driver = webdriver.Firefox(firefox_profile=firefoxProfile, options=opt)

    # Open up the Raleigh page
    driver.get(
        "http://www.redfin.com/city/35711/NC/Raleigh/filter/property-type=house,min-beds=1"
    )
    # have to pause since we added this filter
    time.sleep(5)
    # Click on the "Remove Outline" button to expand our view
    driver.find_element_by_class_name("RemoveOutlineButton").click()
    time.sleep(3)

    # zoom out 2 times to query more homes
    zoomOut = driver.find_element_by_class_name("zoomMinusControlButton")

    for _ in range(3):
        zoomOut.click()
        time.sleep(3)

    # download the current selection
    button = driver.find_element_by_id("download-and-save")

    # increase number saved to 10K
    link = button.get_attribute("href")
    link = link.replace("350", "10000")
    time.sleep(1)

    # Download the csv file
    driver.execute_script(
        'arguments[0].setAttribute("href", arguments[1]);', button, link
    )
    button.click()
    time.sleep(2)
    driver.quit()

    """

    Downloads data from redfin

    """

    # ##################
    # File downloaded #
    # ##################

    filename = max([f for f in os.listdir()], key=os.path.getctime)
    print(filename)
    # move the file into data
    os.rename(filename, f"data/{filename}")
    filename = "data/" + filename
    # also update the file.csv file to be this file
    os.replace(filename, "data/file.csv")

    #################################
    # Removing all unneeded columns #
    #################################

    df = pd.read_csv("data/file.csv")
    df.drop(
        [
            "STATUS",
            "SOLD DATE",
            "NEXT OPEN HOUSE START TIME",
            "NEXT OPEN HOUSE END TIME",
            "FAVORITE",
            "INTERESTED",
            "URL (SEE http://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)",
        ],
        axis=1,
        inplace=True,
    )
    # Sometimes there are homes with year incorrectly listed

    df.to_csv("data/file.csv")


if __name__ == "__main__":
    run()
