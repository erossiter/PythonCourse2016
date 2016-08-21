import tweepy
import time
import imp

twitt = imp.load_source('summer2016', '../../../twitterKeys.py')
twitt.api



## Among a list of twitter users, who is the most _____.
## 'command' must be ascertained by comparing elements of 
## user objects?
def user_activity(user_list, command):
	total = []
	for u in user_list:
		total.append(eval(command))
	index = total.index(max(total))
	return user_list[index].id, user_list[index].name


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


def main():
	## Target twitter user
	target_account = twitt.api.get_user("KittensCam")
 
	## Getting follower and friend object lists
	cat_followers = twitt.api.followers(target_account.id, count = 100)
	cat_friends = twitt.api.friends(target_account.id, count = 100)

	## Among the followers of your target who is the most active?
	print user_activity(cat_followers, "u.statuses_count")

	## Among the followers of your target who is the most popular,
	## i.e. has the greatest number of followers?
	print user_activity(cat_followers, "u.followers_count")

	## Among the friends of your target, i.e. the users she is
	## following, who are the most active layman, expert and celebrity?
	layman, expert, celebrity = categorize_users(cat_friends)
	print user_activity(layman, "u.statuses_count")
	print user_activity(expert, "u.statuses_count")
	print user_activity(celebrity, "u.statuses_count")

	## Among the friends of your target who is the most popular?
	print user_activity(cat_friends, "u.followers_count")

main()

	

