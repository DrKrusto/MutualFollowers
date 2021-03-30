# DrKrusto's Mutual Followers #

### Mutual Followers est un petit script Python qui recherche les followers communs entre plusieurs utilisateurs. ###

Pour trouver ces utilisateurs, on va prendre l'utilisateur avec le plus de followers et on va comparer avec les autres utilisateurs les followers communs jusqu'à avoir les followers communs pour tout ces utilisateurs.

#### Déclaration des clés pour utiliser l'API Twitter.
```
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
api = twitter.Api(consumer_key=consumer_key,
				  consumer_secret=consumer_secret,
				  access_token_key=access_token,
				  access_token_secret=access_secret)
```

#### L'utilisateur déclare les utilisateurs twitter dont il souhaite connaître les followers communs
```
numberFollowers = input("What is the number of users you know the person your looking for is following?\n")
compteur = int(numberFollowers)
listUsers = [ ]
print("Enter " + numberFollowers + " users id below")
while compteur > 0:
	accountId = input()
	listUsers.append(api.GetUser(accountId))
	compteur -= 1
```
#### On détermine l'utilisateur avec le plus de followers et on l'assigne comme étant l'utilisateur principal
```
followerMaxValue = listUsers[0].followers_count
followerMaxAccount = listUsers[0]
for x in listUsers:
	if x.followers_count > followerMaxValue:
		followerMaxValue = x.followers_count
		followerMaxAccount = x
listUsers.remove(followerMaxAccount)
mainListOfFollowersId = api.GetFollowerIDs(followerMaxAccount.id)
```

#### Pour chaque utilisateurs on utilise la fonction intersection qui va chercher les followers communs entre les deux listes de followers
```
for user in listUsers:
	listOfFollowersId = api.GetFollowerIDs(user.id)
	mainListOfFollowersId = set(mainListOfFollowersId).intersection(listOfFollowersId)
```

#### On affiche tout les utilisateurs communs
```
for followersId in mainListOfFollowersId:
	print(api.GetUser(followersId).screen_name)
```
