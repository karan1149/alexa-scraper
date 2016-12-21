# Alexa Scraper
Scrapes the top X sites according to Alexa and prints them as a JSON dictionary mapping URL to rank.

## Usage
To get the first 10 sites using the included top-1m.csv:

```
python scraper.py top-1m.csv 10
```

Output is: 
```
{'yahoo.com': 6, 'google.co.in': 7, 'wikipedia.org': 5, 'youtube.com': 2, 'google.com': 1, 'amazon.com': 8, 'qq.com': 9, 'google.co.jp': 10, 'baidu.com': 4, 'facebook.com': 3}
```
