import tweepy
import time
import imp
import math

twitt = imp.load_source('summer2016', '../../../twitterKeys.py')
twitt.api

## Function that finds all followers/friends of a given user.
## This function is used by 'two_degree_search()'
def search_one(user, command):
	master_list = []
	for page in tweepy.Cursor(eval(command), user.screen_name).pages():
		not_finished = True
		while not_finished:
			try:
				master_list.extend(page)
				not_finished = False
			except tweepy.RateLimitError:
				time.sleep(1)
	return master_list

## Function to generate a master list of user objects including
## those objects supplied in the 'user_list' parameter and all of
## their followers/friends ('command' parameter)
def two_degree_search(user_list, command):
	master_list = user_list
	for u in user_list:
		not_finished = True
		while not_finished:
			try:
				master_list.extend(search_one(u, command))
				not_finished = False
			except tweepy.RateLimitError:
				time.sleep(1)
			except tweepy.TweepError:
				continue
	return master_list

## Function to be flexible to find, among a list of twitter
## users, who is the most active/popular/etc.
def user_activity(user_list, command):
	total = []
	for u in user_list:
		total.append(eval(command))
	index = total.index(max(total))
	return str(user_list[index].screen_name)

## Function to categorize a list of user objects
def categorize_users(user_list):
	layman = []
	expert = []
	celebrity = []
	for u in user_list:
		if u.followers_count < 100:
			layman.append(u)
		elif u.followers_count > 1000:
			celebrity.append(u)
		else:
			expert.append(u)
	return layman, expert, celebrity

def answers():
	target_account = twitt.api.get_user("KittensCam")
 
	## Getting follower and friend object lists
	cat_followers = twitt.api.followers(target_account.id, count = 100)
	cat_friends = twitt.api.friends(target_account.id, count = 100)

	## One degree of separation ##
	print "\nAmong the followers of your target who is the most active?"
	print user_activity(cat_followers, "u.statuses_count")

	print "\nAmong the followers of your target who is the most popular?"
	print user_activity(cat_followers, "u.followers_count")

	print "\nAmong the friends of your target, who are the most active layman, expert and celebrity?"
	cat_friends_layman, cat_friends_expert, cat_friends_celebrity = categorize_users(cat_friends)
	print "Layman: %s" % user_activity(cat_friends_layman, "u.statuses_count")
	print "Expert: %s" % user_activity(cat_friends_expert, "u.statuses_count")
	print "Celebrity: %s" % user_activity(cat_friends_celebrity, "u.statuses_count")

	print "\nAmong the friends of your target who is the most popular?"
	print user_activity(cat_friends, "u.followers_count")

	## Two degrees of separation ##
	print "\nAmong the followers of your target and their followers, who is the most active?"
	cat_followers_layman, cat_followers_expert, cat_followers_celebrity = categorize_users(cat_followers)
	master_list_followers = two_degree_search((cat_followers_layman + cat_followers_expert), "twitt.api.followers")
	all_followers_layman, all_followers_expert, all_followers_celebrity = categorize_users(master_list_followers)
	print user_activity((all_followers_layman + all_followers_expert), "u.statuses_count")

	print "\nAmong the friends of your target and their friends, who is the most active?"
	master_list_friends = two_degree_search((cat_friends_layman + cat_friends_expert), "twitt.api.followers")
	all_friends_layman, all_friends_expert, all_friends_celebrity = categorize_users(master_list_friends)
	print user_activity((all_friends_layman + all_friends_expert), "u.statuses_count")


answers()



	

