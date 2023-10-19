#This script is used for Web Scraping using BeautifulSoup and Requests objects
#Using find and find_all method
#Author : Ashwin
#Date : 18-Oct-2023

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.scrapethissite.com/pages/forms/"

# https://www.scrapethissite.com/pages/forms/robots.txt

#Fetch the web page and store the response code [200]
page = requests.get(url)
print(page)

#Create a BeautifulSoup object and Change html to Python friendly format
soup = BeautifulSoup(page.text, "html.parser")
#parser-lxml = Change html to Python friendly format
#soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

#Print the title of the page
print(soup.title.string)

#Find specific objects of html
#print(soup.find("div"))
#print(soup.find_all("div", class_ = "col-md-12"))

#Find and print all the links in the page
#for link in soup.find_all("a"):
#    print(link.get("href"))

#Find and print all the data from the table in the page
srctable = soup.find('table', class_ = 'table')
#print(srctable)

#Obtain every title of columns with tag <th> and append to list
headers_list = []
for i in srctable.find_all('th'):
    title = i.text
    headers_list.append(title)

#print(headers_list)

team_name_list = []
for i in srctable.find_all('td', class_ = 'name'):
    name = i.text
    team_name_list.append(name)

#print(team_name_list)

year_list = []
for i in srctable.find_all('td', class_ = 'year'):
    year = i.text
    year_list.append(year)

wins_list = []
for i in srctable.find_all('td', class_ = 'wins'):
    wins = i.text
    wins_list.append(wins)

losses_list = []
for i in srctable.find_all('td', class_ = 'losses'):
    losses = i.text
    losses_list.append(losses)

#Create a datafram
#mydata = pd.DataFrame(columns = headers)
mydata = pd.DataFrame({'Team Name':team_name_list, 'Year':year_list, 'Wins':wins_list, 'Losses':losses_list})
#print(mydata)

#Export to csv file
mydata.to_csv('Hockey_Teams_NHL_stats.csv', index=False)

#Try to read csv
mydata2 = pd.read_csv('Hockey_Teams_NHL_stats.csv')
print(mydata2)
