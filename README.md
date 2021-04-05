## Simple BOJ Web Crawler

#### Tested only on Chrome
+ You may need
  + Chromedriver (version will be depend on of your chrome version)
    + https://chromedriver.chromium.org/downloads
  + input.xlsx
    + ouput.xlsx must refer to input.xlsx because it needs to know pre-data to check
      + Solved problems
      + Rank
      + Absent

#### Modules
```
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import openpyxl
```
+ Selenium and BeautifulSoup are used for web crawling
+ Pandas -> can handle excel and csv files as dataframe
+ Time is used to check whether user has signed in acmicpc.net or not
+ openpyxl is to wipe out dependency problem

#### Output
+ output.txt
  + Raw data, crawled from Web site
+ output.xlsx
  + Processed data, saved as xlsx format
