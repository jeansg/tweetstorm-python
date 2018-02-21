#!/usr/bin/python
# filename: TweetStorm.py

# -*- encoding:utf8 -*-

__author__ = "Jean Guirro (jean.guirro@hotmail.com)"
__version__ = "1.0"
__date__ = "$Date: 2018/02/20 10:47:00 $"
__license__ = "Python"
__status__ = "Test"

# Modules needed
from os import getenv
import sys
import getopt
import tweepy
import config
import ConfigParser
from ConfigParser import SafeConfigParser

# Help.
def usage():
    print '\n  Usage: '+sys.argv[0]+' "Arguments" "Text"\
\n\n\t-k [Consumer Key]\
\n\t-s [Consumer Secret]\
\n\t-a [Acess Token]\
\n\t-t [Acess Token Secret]\
\n\tor with config file\
\n\t-C [Config file]\
\n\t\nExamples:\
\n\t $ ./TweetStorm.py -k "ConsumerKey" -s "ConsumerSecret" -a "AcessToken" -t "AcessTokenSecret" "LONGTEXT"\
\n\t $ ./TweetStorm.py -C twitter_api.ini "LONGTEXT"\
\n'

# Twitter api authentication
def api_auth(key,csecret,token,tsecret):
    auth = tweepy.OAuthHandler(key, csecret)
    auth.set_access_token(token, tsecret)
    return tweepy.API(auth)

# Text split 
def tweet_split(msg):
	words = msg.split()
	tweet = ''
	list = []
	if len(words[0]) > 140:
		for i in range(0, len(words[0]), 135):
			tweet = words[0][i: i + 135]
			list.append(tweet)
	else:
	# Avoid to have a broken/nonsense sentence in the tweet
		for i in range(len(words)):
			tweet += words[i]
			if len(tweet + words[i]) > 135:
				list.append(tweet)
				tweet = ''
			else:
				if i == len(words) - 1:
					list.append(tweet)
				else:
					tweet += ' '

        # Tweet index: add tweet#/total at the beginning
	for i in range(len(list)):
		list[i] = str(i + 1) + '/' + str(len(list)) + ': ' + list[i]
	return(list)

def main():
    # Verify arguments
    try:
        Optargs, Args = getopt.getopt(sys.argv[1:],"k:s:a:t:C:",["key=","cs_secret=","token=","token_secret=","config="])
    except getopt.GetoptError, error:
        sys.exit(usage())
    if not Optargs:
        sys.exit(usage())

    # Feed arguments into variables
    for Optarg, Arg in Optargs:
        if Optarg in ("-k","--CS_KEY"):
            CS_key=Arg
        elif Optarg in ("-s","--CS_SECRET"):
            CS_secret=Arg
        elif Optarg in ("-a","--ACESS_TOKEN"):
            Token=Arg
        elif Optarg in ("-t","--TOKEN_SECRET"):
            Token_secret=Arg
        elif Optarg in ("-C","--config"):
            CONF=Arg
        else:
            sys.exit(usage())

    # Parse config file
    try:
        CONF
        parser = SafeConfigParser()
        parser.read(CONF)
        CS_key = parser.get('TWITTER', 'CONSUMERKEY')
        CS_secret = parser.get('TWITTER', 'CONSUMERSECRET')
        Token = parser.get('TWITTER', 'ACCESSTOKEN')
        Token_secret = parser.get('TWITTER', 'ACCESSTOKENSECRET')
    except NameError:
        CONF = ""

    # Test given arguments
    try:
        CS_key
    except NameError:
        print '\n ERROR: Verify if Customer Key was informed \n'
        sys.exit(1)
    try:
        CS_secret
    except NameError:
        print '\n ERROR: Verify if Customer Secret was informed \n'
        sys.exit(1)
    try:
        Token
    except NameError:
        print '\n ERROR: Verify if Access Token was informed \n'
        sys.exit(1)
    try:
        Token_secret
    except NameError:
        print '\n ERROR: Verify if Access Token Secret was informed \n'
        sys.exit(1)
    try:
        api = api_auth(CS_key,CS_secret,Token,Token_secret)
        longstring = sys.argv[-1]
        print(longstring)
        tweets = tweet_split(longstring)
        for i in range(len(tweets)):
            status = status = api.update_status(status=tweets[i])
    except tweepy.TweepError as e:
        print ("Error when sending tweet: %s" % e)

	
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print 'Killed by user'
        sys.exit(0)
