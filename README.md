# Python Tweetstorm
It's a way to bypass Twitter's limitation of 140 chars, splitting the given text into numbered tweets

## Requirements

Twitter key and tokens
> Twitter Application: https://apps.twitter.com/app

Python (2.7) modules:  
- tweepy  
- sys  
- getop  
- config  
- ConfigParser  

## Usage
```
Usage: ./TweetStorm.py "Arguments" "Text"
	-k [Consumer Key]
	-s [Consumer Secret]
	-a [Acess Token]
	-t [Acess Token Secret]
	or with config file
	-C [Config file]
```
	
### Examples:
>	 $ ./TweetStorm.py -k "ConsumerKey" -s "ConsumerSecret" -a "AcessToken" -t "AcessTokenSecret" "LONGTEXT"


#### Utilizing config file
File example:

```
[TWITTER]
ConsumerKey = example
ConsumerSecret = example
AccessToken = example
AccessTokenSecret = example
```

>        $ ./TweetStorm.py -C twitter_api.ini "LONGTEXT"

