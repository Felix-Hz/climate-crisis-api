# Twitter Data Scraping for Climate Crisis Sentiment Analysis
## Introduction

This repository contains Python code for scraping data from Twitter's API to create a dataset focusing on people's attitudes and opinions on the climate crisis. The collected data can then be used as a prototype for conducting sentiment analysis. This documentation provides an overview of the project structure, installation instructions, usage guidelines, and additional information.

## Disclaimer

Twitter's terms of service prohibit users from "scraping, crawling, or using any automated means to access the Services or Content." However, Twitter does provide an exception for "non-commercial research or analysis." This means that you can scrape Twitter's HTML for personal or research purposes without violating the terms of service while scraping public data:

 

>    *Non-Commercial Use.* You may use the Services and Content for non-commercial research or analysis purposes, provided that you comply with all of the terms of this Agreement. For example, you may use the Services and Content to conduct surveys, analyze trends, or develop new products or services. However, you may not use the Services and Content for any commercial purpose, such as to sell advertising, market products or services, or generate leads.

>    *Commercial Use.* If you wish to use the Services and Content for any commercial purpose, you must obtain a license from Twitter.

You can find the full terms of service here: https://developer.twitter.com/en/developer-terms/agreement-and-policy


## Installation

### To use this repository, follow these steps:

1. Clone the repository to your local machine:

`git clone https://github.com/your-username/twitter-climate-sentiment.git`

2. Install the required dependencies:

    `cd twitter-climate-sentiment`
    `pip install -r requirements.txt`

3. Set up your Twitter API credentials:
        - Create a Twitter Developer account if you don't have one.
        - Generate API keys (consumer key, consumer secret, access token, access token secret) from the Twitter Developer portal.
        - Update the config.py file with your API credentials.

4. Install and set up a database (optional):
        - If you want to store the scraped data in a database, ensure you have a compatible database system (e.g., MySQL, PostgreSQL) installed.
        - Update the database configuration in config.py with your credentials.

## Usage

1. Open the command line interface and navigate to the repository directory:

`cd twitter-climate-sentiment`

2. Modify the parameters in the config.py file according to your requirements. Adjust search keywords, date range, and other settings to tailor the data collection process.

3. Run the data scraping script:

    `python scrape_tweets.py`

    - This script will initiate the data scraping process and fetch tweets related to the climate crisis based on the specified criteria. The collected data will be stored either in a database (if configured) or in a CSV file.

4. Once the data collection is complete, you can proceed to perform sentiment analysis on the dataset using various Python libraries and techniques. Refer to the sentiment analysis documentation or example code provided within the repository for further guidance.

## Project Structure

The repository is structured as follows:

    - scrape_tweets.py: The main script responsible for connecting to the Twitter API, retrieving tweets, and storing them in a database or CSV file.
    - config.py: Configuration file containing Twitter API credentials, database connection details, and other settings.
    - requirements.txt: A list of required Python packages for easy installation.
    - data/: Directory to store the scraped data (CSV files, database schema, etc.).
    - sentiment_analysis/: Directory containing example code or scripts related to sentiment analysis on the collected data.

## Additional Notes

    Be mindful of Twitter's API usage guidelines and rate limits. Excessive or abusive scraping can result in account suspension or other restrictions.
    Ensure compliance with data privacy regulations and ethical considerations when working with user-generated data from Twitter.
    Consider using a virtual environment to isolate the project dependencies from your system-wide Python installation.
    Make sure to acknowledge the limitations and biases inherent in sentiment analysis techniques and the use of social media data.

## Resources

    - Twitter Developer Portal: https://developer.twitter.com
    - Python Twitter API Wrapper (Tweepy): https://github.com/tweepy/tweepy

Please refer to the official documentation of the respective resources for more detailed information.

*Note:* Remember to review the licensing and terms of use of any third-party libraries or resources utilized in this project to ensure compliance with their respective terms and conditions.