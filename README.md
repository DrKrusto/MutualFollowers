# DrKrusto's Mutual Followers #

## English doc

### Mutual Followers is a small Python script which fetch all the mutual followers of multiple users. ###

To find these users, we are going to take the user which has the most followers and we will compare this one with all the other users' followers until we have all the mutual followers for all these users.

#### The user enters all the twitter uses he wants to know the mutual followers from
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

#### We define which users has the most followers and we assign him/her as being the primary user
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

#### For each users we use the function intersection which will seek all the mutual followers between the two lists of followers
```
for user in listUsers:
	listOfFollowersId = api.GetFollowerIDs(user.id)
	mainListOfFollowersId = set(mainListOfFollowersId).intersection(listOfFollowersId)
```

#### We print all the mutual followers
```
for followersId in mainListOfFollowersId:
	print(api.GetUser(followersId).screen_name)
```

## Documentation en français

### Mutual Followers est un petit script Python qui recherche les followers communs entre plusieurs utilisateurs. ###

Pour trouver ces utilisateurs, on va prendre l'utilisateur avec le plus de followers et on va comparer avec les autres utilisateurs les followers communs jusqu'à avoir les followers communs pour tout ces utilisateurs.

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
