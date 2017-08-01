#Register an app: https://dev.twitter.com/

#sudo pip install tweepy
import tweepy
import time

#Check the documentation page
#http://docs.tweepy.org/en/v3.2.0/

#Get access to API
<<<<<<< HEAD
#auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret') ##Never put these in public code! Do NOT push keys to GitHub. Keep a private file that you can simply import
#auth.set_access_token('your access token', 'your access token secret')    
#api = tweepy.API(auth)

import imp
twitt = imp.load_source('summer2016', '/Users/erinrossiter/Dropbox/Summer2016/googleKeys.py')
twitt.api


#See rate limit
twitt.api.rate_limit_status()

#Create user objects
#betuld = twitt.api.get_user('elrossit1')
#krugman = twitt.api.get_user('NYTimeskrugman')


#What can I do using this object?
#dir(betuld)

#Get some of her information
#betuld.id
#betuld.name
#betuld.screen_name
#betuld.location
#betuld.profile_location

#dave=twitt.api.get_user('jabbersoccer')
#dave.profile_image_url

#Check her tweets
#betuld.status
#betuld.status.text
#betuld.statuses_count
#dave.statuses_count

#Check her followers
#betuld.followers_count
#betuld.followers() #creates a list of user objects - only the first 20!
#type(betuld.followers()[0])
#betuld.followers()[0].screen_name #the results are user result sets as well
#twitt.api.followers(betuld.id,count=200) #creates a list of user objects - can get up to 200

#betuld.followers_ids() #creates a list of user ids - up to 5000
#twitt.api.followers_ids('BetulD_')
don = twitt.api.get_user('realDonaldTrump')

def myFunc():
	for follower_id in don.followers_ids():
		user = twitt.api.get_user(follower_id)
		print user.screen_name

try:
	myFunc()
except Exception, TweepError:
	sys.sleep(60)
	myFunc()
finally:
	pass
=======
auth = tweepy.OAuthHandler('your consumer key', 'your consumer secret') ##Never put these in public code! Do NOT push keys to GitHub. Keep a private file that you can simply import
auth.set_access_token('your access token', 'your access token secret')    
api = tweepy.API(auth)

#import imp
#twitt=imp.load_source('twitt', '/home/david/Dropbox/Code/twitter_api.py')
#twitt.api


#See rate limit
api.rate_limit_status()

#Create user objects
betuld = api.get_user('BetulD_')
krugman = api.get_user('NYTimeskrugman')

#What can I do using this object?
dir(betuld)

#Get some of her information
betuld.id
betuld.name
betuld.screen_name
betuld.location
betuld.profile_location

dave=api.get_user('jabbersoccer')
dave.profile_image_url

#Check her tweets
betuld.status
betuld.status.text
betuld.statuses_count
dave.statuses_count

#Check her followers
betuld.followers_count
betuld.followers() #creates a list of user objects - only the first 20!
type(betuld.followers()[0])
betuld.followers()[0].screen_name #the results are user result sets as well
api.followers(betuld.id,count=200) #creates a list of user objects - can get up to 200

betuld.followers_ids() #creates a list of user ids - up to 5000
api.followers_ids('BetulD_')

for follower_id in betuld.followers_ids():
	user = api.get_user(follower_id)
	print user.screen_name
>>>>>>> carlson9/master

#How to deal with limits

#Get the first 2 "pages" of follower ids
<<<<<<< HEAD
#krugmans_followers=[]

#for page in tweepy.Cursor(twitt.api.followers_ids, 'NYTimeskrugman').pages(2):
#    krugmans_followers.extend(page) #extend is like extend, but can take arguments with length greater than 1
#    time.sleep(60)
    
#Get the ids of 6000 followers
#krugmans_followers=[]

#for item in tweepy.Cursor(twitt.api.followers_ids, 'NYTimeskrugman').items(6000):
#	print item
#	krugmans_followers.append(item)
#	time.sleep(1)
=======
krugmans_followers=[]

for page in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').pages(2):
    krugmans_followers.extend(page) #extend is like extend, but can take arguments with length greater than 1
    time.sleep(60)
    
#Get the ids of 6000 followers
krugmans_followers=[]

for item in tweepy.Cursor(api.followers_ids, 'NYTimeskrugman').items(6000):
	print item
	krugmans_followers.append(item)
	time.sleep(1)
>>>>>>> carlson9/master
	
###If you are running code, this time.sleep will not gaurantee you don't go over the limit.
# Exercise: write generic code that will never break (this will be very helpful for everything you do, including the homework)



<<<<<<< HEAD



=======
>>>>>>> carlson9/master
