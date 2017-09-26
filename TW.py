#!/usr/bin/python3

from TwitterAPI import TwitterAPI

CONSUMER_KEY = 'G5VEfOdfZC2BpVNN3VmIXhmp1'
CONSUMER_SECRET = '2aUoYnMXSjhIGuBATwmamFnK7rb2CCs4eRFbYpcaVn33bhcosq'
ACCESS_TOKEN_KEY = '910781772824068097-4UctxNpBE7ZCS0PcdKk18UwQ0oWyAhV'
ACCESS_TOKEN_SECRET = 'TZcDnfeK6oFNsUOumAWWCHMAGPOQUatAWrxDMJZvdb6D9'

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
file = open('/home/pi/Desktop/picamera', 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'pic from pyhton script'}, {'media[]':data})
print(r.status_code)
