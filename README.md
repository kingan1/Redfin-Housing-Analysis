# Redfin Housing Analysis

Project completed for CS 3535, Web Scraping in my undergrad at Appalachian State University.

The goals of this project was to extract large amounts of data from the web using web scraping tools, clean the data, create visuals, and use machine learning techniques.

# How to run
1. First, to ensure all libraries are installed, run `pip install -r requirements.txt`
2. To run the program, you should first run `python redfin.py`
    + note: only run this if you want to generate a fresh .csv file. If not, the program will use the existing file in data/file.csv
    + This starts a selenium browser which navigates to redfin and downloads a csv file of listings in Raleigh, NC
    + This will produce csv and json files to be stored in data
    + The json was created for class requirements, but is not used in later files.
3. To produce images, run `python image.py`
    + This produces 5 images, attempting to describe the data and possible patterns.
4. To build machine learning models, run `python model.py`
    + this first performs data cleaning, and then builds and compares several machine learning models, including
        + Linear Regression
        + Ridge Regression
        + Extra Trees Regressor
        + Elastic Net
        + Gradient Boosting Regressor

# Future work
+ Re-evaluate better ways to visualize
+ Improve model results
+ Explore more pre-processing
