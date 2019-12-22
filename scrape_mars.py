#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars 

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


# In[2]:

def scrape_info(): 
    # chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # NASA Mars News

    # In[3]:


    # Visit https://mars.nasa.gov/news/
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")


    # In[4]:


    # Get the news title
    news_title = soup.find('div', class_='content_title').text

    # Get the news blurb
    news_p = soup.find('div', class_='article_teaser_body').text


    # In[5]:


    # Collect the latest News Title and Paragraph Text
    # Assign the text to variables that you can reference later 
        
    print(news_title) 
    print(news_p)


    # Mars Space Images - Featured Image

    # In[6]:


    # Navigate the site and find the image url for the current Featured Mars Image
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    time.sleep(3)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")


    # In[7]:


    browser.click_link_by_partial_text("FULL")

    time.sleep(3)

    # # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")


    # In[8]:


    browser.click_link_by_partial_text("more info")
    time.sleep(3)

    # # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    featured_image_url = soup.find('img', class_= "main_image")["src"]
    mars_image = "https://www.jpl.nasa.gov/" + featured_image_url


    # Mars Weather

    # In[9]:


    # Navigate the site and find the latest tweet with the latest weather on Mars
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    mars_weather = soup.find('p', class_= "TweetTextSize").text

    # print(mars_weather)


    # Mars Facts

    # In[10]:


    # Navigate the site and find the url for Mars Facts
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)


    # In[11]:


    #Read table into a dataframe and extract to html  
    table = pd.read_html(facts_url)[0]
    table.columns = ["Description", "Value"]
    table.set_index("Description", inplace=True)
    
    # convert to html and add classes
    mars_facts = table.to_html(classes="table table-striped")
    
    # print(mars_facts)


    # Mars Hemispheres

    # In[21]:


    # Navigate the site and find the url for Mars Hemisphere information
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)

    time.sleep(3)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")


    # In[24]:


    # create an empty list for us to add to as we iterate through all the hemisphere links 
    hemisphere_img = []

    names = ["Cerberus", "Schiaparelli", "Syrtis", "Valles"]

    #search for the different hemisphere links looking for "h3" tag
    # hemispheres = soup.find_all("h3")

    #create a for loop that will go through each link, grab the 'sample' image link and the title 
    for x in names:
        hemisphere = {}
        browser.click_link_by_partial_text(x)
        
        time.sleep(3)
        
        html = browser.html
        soup = bs(html, "html.parser")
        
        # use "Sample" to then grab the href 
        img = soup.find("a", text = "Sample").get("href")
        hemisphere["img_url"] = img
        
        # get the title for each page
        hemisphere["title"] = soup.find("h2", class_ = "title").text
        
        # append information to list we created 
        hemisphere_img.append(hemisphere)
        
        # go back 
        browser.back()

    # print out the list of dictionaries 
    # print(hemisphere_img)
    

    mars_stuff = {
        "News_Title": news_title, 
        "News_Blurb": news_p, 
        "Mars_Image": mars_image, 
        "Mars_Weather": mars_weather, 
        "Mars_Facts": mars_facts,
        "Hemisphere_Images": hemisphere_img
    }
    # print out the list of dictionaries 
    # print(hemisphere_img)
    return mars_stuff


# In[ ]:




