import twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
api = twitter.Api(consumer_key=consumer_key,
				  consumer_secret=consumer_secret,
				  access_token_key=access_token,
				  access_token_secret=access_secret)

numberFollowers = input("What is the number of users you know the person your looking for is following?\n")
compteur = int(numberFollowers)
listUsers = [ ]
print("Enter " + numberFollowers + " users id below")
while compteur > 0:
	accountId = input()
	listUsers.append(api.GetUser(accountId))
	compteur -= 1
# theses lines will be used to seek which account has the less amount of followers #	
followerMaxValue = listUsers[0].followers_count
followerMaxAccount = listUsers[0]
for x in listUsers:
	if x.followers_count > followerMaxValue:
		followerMaxValue = x.followers_count
		followerMaxAccount = x
listUsers.remove(followerMaxAccount)
mainListOfFollowersId = api.GetFollowerIDs(followerMaxAccount.id)
for user in listUsers:
	listOfFollowersId = api.GetFollowerIDs(user.id)
	mainListOfFollowersId = set(mainListOfFollowersId).intersection(listOfFollowersId)
#	for followerLesserUser in mainListOfFollowersId:
#		followerApproved = False
#		for followersUser in listeIdFollowers:
#			if followersUser == followerLesserUser:
#				followerApproved = True
#		if followerApproved == False:
#			mainListOfFollowersId.remove(followerLesserUser)
for followersId in mainListOfFollowersId:
	print(api.GetUser(followersId).screen_name)