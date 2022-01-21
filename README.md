<div align="center">

    
# README

### by Joann Balraj 
### January 24, 2022

</div align="center">
    
<hr style="border:3px solid black"> </hr>

# Project Description
#### "Some say climate change is the biggest threat of our age while others say it’s a myth based on dodgy science. We are turning some of the data over to you so you can form your own view."  - https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data

### What is this?
> "We have repackaged the data from a newer compilation put together by the Berkeley Earth, which is affiliated with Lawrence Berkeley National Laboratory. The Berkeley Earth Surface Temperature Study combines 1.6 billion temperature reports from 16 pre-existing archives. It is nicely packaged and allows for slicing into interesting subsets (for example by country). They publish the source data and the code for the transformations they applied. They also use methods that allow weather observations from shorter time series to be included, meaning fewer observations need to be thrown away." - https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data

### Overview & Plan:
> I am going to be choosing a major city from the Berkeley Earth temperatures data set.  After preparing and exploring the data, I will use time series forecasting methods to predict average temperatures of Mexico City. After comparing the different forecasting models, I will select the best performing model to run on the test data to predict future temperatures and see how well it performed.

<hr style="border:2px solid black"> </hr>

# Project Goals:
- Use the earth surface temperature data offered by Berkeley Earth through Kaggle.com. 
- Select one location, could be a city or a state or something relatively similar in size and analyze the patterns in temperature over time. 
- Model those patterns to forecast temperature into the future.


<hr style="border:2px solid black"> </hr>

# Project Planning
## Plan -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

<b>Planning:</b>  
- Create a README file (check!)
- Ensure my wrangle.py modules are well documents and functional
- Link to my trello planning board: https://trello.com/invite/b/5ifN7CAH/94a29a2bc5711e4921c5241f570a6328/time-series-analysis-project

<b>Acquisition </b>  
- Gather earth surface temp data (.csv) from https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data 
- Create a `wrangle.py` file to make future acquisition easier

<b>Preparation</b>  
- Create a `workbook.ipynb` file to put all work in 
- Clean aquired temperature data:
    - remove missing values, 
    - inspect data integrity issues 
    - ensure columns are proper data type
    - reduce outliers
- Create a scale function for future modeling
- Create split function for future modeling
- Add all new functions to `wrangle.py`

<b>Exploration and Pre-processing</b>  
- Explore the target variable using visualization and statistical testing
- Use clustering methodologies to explore the data and attempt at least 3 combinations of features
- Summarize takeaways and conclusions

<b>Modeling</b>  
- Split data appropriately 
- Establish and evaluate baseline model
- Create at least 4 different models and compare their performance

<b>Modeling</b>  
- Deliver presentation
- Be prepared to answer questions about code and presentation



<hr style="border:2px solid black"> </hr>

# Data Dictionary

| Feature                       | Datatype                  | Description                                                        |
|:------------------------------|:--------------------------|:-------------------------------------------------------------------|
| dt                            | 239177 non-null  object   | Date
| AverageTemperature            | 228175 non-null  float64  | Average land temperature in celsius
| AverageTemperatureUncertainty | 228175 non-null  float64  | The 95% confidence interval around the average temperature
| City                          | 239177 non-null  object   | City data is from  
| Country                       | 239177 non-null  object   | Country data is from
| Latitude                      | 239177 non-null  object   | Latitude for where the data is from
| Longitude                     | 239177 non-null  object   | Longitude for where the data is from

<hr style="border:2px solid blue"> </hr>

# Steps to Reproduce

You will need to obtain the `GlobalLandTemperaturesByMajorCity.csv` file from https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data to use for the project.

 1. Read this README.md (check!)
 2. Download at the `wrangle.py` and `Final_Report.ipynb` file into your working directory.
 3. Create a `.gitignore` for your `env.py` file.
 4. Add your own `env.py` file to your directory with username, password, and host address. 
 5. Run the `Final_Report.ipynb` in a jupyter notebook.
