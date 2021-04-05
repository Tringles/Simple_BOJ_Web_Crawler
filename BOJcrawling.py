from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import openpyxl


pd.set_option('mode.chained_assignment',  None)


driver = webdriver.Chrome('/Users/jongminjung/Desktop/L/Univ./Toy/Crawling/chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.acmicpc.net/login')

while True:
    time.sleep(3)
    if driver.current_url != 'https://www.acmicpc.net/login':
        break

driver.get('https://www.acmicpc.net/group/ranklist/10895')

elements = driver.find_elements_by_tag_name('td')

f = open('output.txt', 'w', encoding='utf-8')
cnt = 4
for n in elements:
    cnt+=1
    if cnt % 6 == 0:
        f.write(n.text + '\t')
    if cnt % 6 == 2:
        f.write(n.text + '\n')
f.close()

crawled = pd.read_csv('output.txt', names=['ID', 'Solved'], delimiter = '\t')


df=pd.read_excel('input.xlsx', engine = 'openpyxl')
end = df.index.size
cnt = 1
for i in range(0, end):
    tmp = df.loc[i][['아이디', 'D - day']].values
    for j in range(0, end):
        temp = crawled.loc[j][['ID', 'Solved']].values
        if tmp[0] == temp[0]:
            df['D - 1'][i] = df['D - day'][i]
            df['D - day'][i] = crawled['Solved'][j]
            df['Today Sol'][i] = df['D - day'][i] - df['D - 1'][i]
            if df['Today Sol'][i] <= 0 and df['결석 횟수'][i] != -1:
                df['결석 횟수'][i] += 1
            df['등수 등락'][i] = i - j
            df['이전 등수'][i] = df['현재 등수'][i]
            df['현재 등수'][i] -= (i-j)
            df['Total Solved'][i] += df['Today Sol'][i]
            break

df.sort_values(by=['현재 등수'], inplace=True)
df.to_excel('output.xlsx', index=False)
