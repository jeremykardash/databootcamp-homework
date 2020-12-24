# Import Dependencies 
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import os
from webdriver_manager.chrome import ChromeDriverManager
os.chmod('/Users/jerkardash/Data/databootcamp-homework/Unit 11 - Web Scraping/chromedriver', 755)

def init_browser():
    #Path is specific to each user and must be replaced with your path to the chromedriver
    executable_path = {'executable_path': '/Users/jerkardash/Data/databootcamp-homework/Unit 11 - Web Scraping/chromedriver'} #ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

#Create dictionary to be imported into mongoDB
mars_info = {}

def mars_news():
    try:

        #Initialize browser
        browser = init_browser()

        #Visit NASA Mars News through splinter
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        #HTML Object and Parse with BS
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        #Produce date, title and paragraph snippet
        date = soup.find('div', class_='list_date').text
        news_title = soup.find_all('div', class_='content_title')[1]
        news_title_text = news_title.find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text

        #Import into dictionary
        mars_info['news_date'] = date
        mars_info['news_title'] = news_title_text
        mars_info['news_teaser'] = news_p

        return mars_info
    
    finally:
        
        #Close browser when scrape compelte
        browser.quit()


def mars_image():
    try:

        #Initialize browser
        browser = init_browser()

        #JPL Mars Images
        url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)

        #HTML Object and Parse with BS
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        #Produce image url
        featured_image_url  = soup.find('article')['style'].replace('background-image: url(', '').replace(');', '')[1:-1]
        main_url =" https://www.jpl.nasa.gov"
        full_url = main_url + featured_image_url

        #Import into dictionary
        mars_info["image_url"] = full_url

        return mars_info

    finally:

        #Close browser when scrape compelte
        browser.quit()

def mars_facts():
    try:
        #Initialize browser
        browser = init_browser()

        #Mars Facts
        url = 'https://space-facts.com/mars/'
        mars_facts = pd.read_html(url)

        #Get mars facts in dataframe
        mars_df = mars_facts[0]

        #Assign columns
        mars_df.columns = ["Description", "Value"]

        #Set index to desciption without indexing
        mars_df.set_index("Description", inplace=True)

        #make html file a variable
        html = mars_df.to_html()
        
        #Import mars facts into dictionary
        mars_info["mars_facts"] = html

        return mars_info

    finally:

        #Close browser when scrape compelte
        browser.quit()

def mars_hemispheres():
    try:

        #Initialize browser
        browser = init_browser()

        #Mars Hemispheres
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)

        #HTML Object and Parse with BS
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        #Url and list for later use
        main_url = 'https://astrogeology.usgs.gov'
        hemispheres = []

        #Find every instance of a hemisphere, and create for loop
        items = soup.find_all('div', class_='item')
        for i in items:
            
            #Retreive title and image url, visit the url by combining with main URL
            title  = i.find('h3').text
            image_url = i.find('a', class_='itemLink product-item')['href']
            browser.visit(main_url + image_url)
            
            #Browse the indidvudal HTML and access the full size image
            image_html = browser.html
            soup = BeautifulSoup(image_html, 'html.parser')
            img_url = main_url + soup.find('img', class_='wide-image')['src']
            
            #Append to list of dictionaries 
            hemispheres.append({"title" : title, "img_url" : img_url})

        mars_info['hemispheres'] = hemispheres

        return mars_info
    
    finally:

        #Close browser when scrape compelte
        browser.quit()