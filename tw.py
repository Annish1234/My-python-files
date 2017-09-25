#!/usr/bin/python3
# importing the module
import tweepy 
 
# personal details
consumer_key ="G5VEfOdfZC2BpVNN3VmIXhmp1"
consumer_secret ="2aUoYnMXSjhIGuBATwmamFnK7rb2CCs4eRFbYpcaVn33bhcosq"

access_token ="910781772824068097-4UctxNpBE7ZCS0PcdKk18UwQ0oWyAhV"
access_token_secret ="TZcDnfeK6oFNsUOumAWWCHMAGPOQUatAWrxDMJZvdb6D9"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
