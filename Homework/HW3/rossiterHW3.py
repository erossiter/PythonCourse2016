import tweepy
import time
import imp

twitt = imp.load_source('summer2016', '../../../twitterKeys.py')
twitt.api





## Among the followers of your target who is the most active?
## pass this function an object 
def how_active(user_obj):
	return user_obj.statuses_count



## Among the followers of your target who is the most popular,
## i.e. has the greatest number of followers?



def main():
	## Target twitter user
	target_account = twitt.api.get_user("KittensCam")
 
	## Getting follower objects
	cat_lovers = twitt.api.followers(target_account.id, count = 100)
	
	for i in cat_lovers:
		how_active(i)
		
