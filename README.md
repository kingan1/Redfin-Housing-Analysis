To run the program, you should first run redfin.py
This produces both a .csv and .json but the .csv is the accurate/correct file

From there, you should run image.py if you want images based on the data
or model.py if you want to see 5 different models of computation and their results

This project scrapes ~10K homes from redfins website centered around Raleigh and collects data about each home.
My visuals then explore the overall data, such as where they are located and then explores relationships between price and
several columns. My model then tries to predict housing prices based on several columns, and outputs its RMSE.