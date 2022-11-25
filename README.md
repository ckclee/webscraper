# DevProjects - Web scraper to get news article content
- build a simple web scraper that will return the content of a news article when given a specific URL. Some examples of real products which use similar technologies include price-tracking websites and SEO audit tools which may scrape top search results.

## Requirements

Choose one news website - see article examples below for inspiration. Given a specific article URL from the website of your choice, return the title and content of the article to the user.
I wrote this program to work with washingtonpost.com urls only.
Examples article URLs:
https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/
https://www.washingtonpost.com/technology/2022/11/23/mars-rover-rock-samples/
https://www.washingtonpost.com/technology/2022/11/24/twitter-musk-reverses-suspensions/

For an extra challenge: Parse out information such as the article title, updated date, and byline to return separately to the user.

## Tech/framework used
Built with Python3

## How to use
Just run in the terminal inside the repo directory:

```bash
> python3 scrape.py news_url
```

Example:
```bash
> python3 scrape.py https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
Most open source projects use the MIT license. Feel free to choose whichever license you prefer.
