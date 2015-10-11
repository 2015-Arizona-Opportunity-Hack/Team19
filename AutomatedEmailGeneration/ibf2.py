__author__ = 'Swetha Baskaran'
import json

def loadDataset2(path=""):
	""" To load the dataSet"
		Parameter: The folder where the data files are stored
		Return: the dictionary with the data
	"""

	#Load the data
	don=[]
	count = 0 
	for line in open(path+"Donor-Prod-Ratings2.csv"):
		line = line.replace('"', "")
		line = line.replace("\\","")
		(donor,prod,rating) = line.split(",")
		if float(rating) > 0.0:
			don.append((donor))
	return don


def loadDataset3(path=""):
	""" To load the dataSet"
		Parameter: The folder where the data files are stored
		Return: the dictionary with the data
	"""

	#Load the data
	pro=[]
 
 	count = 0 
	for line in open(path+"Donor-Prod-Ratings2.csv"):
		line = line.replace('"', "")
		line = line.replace("\\","")
		(donor,prod,rating) = line.split(",")
		if float(rating) > 0.0:
			pro.append((prod))
	return pro

def loadDataset4(path=""):
	""" To load the dataSet"
		Parameter: The folder where the data files are stored
		Return: the dictionary with the data
	"""

	#Load the data
	prefs = {}
	count = 0
	for line in open(path+"Donor-Prod-Ratings2.csv"):
		line = line.replace('"', "")
		line = line.replace("\\","")
		(donor,prod,rating) = line.split(",")
		try:
			if float(rating) > 0.0:
				prefs.setdefault(prod,{})
				prefs[prod][donor] = float(rating)
		except ValueError:
			count+=1
			print "value error found! " + donor + prod + rating
		except KeyError:
			count +=1
			print "key error found! " + donor + " " + prod
	return prefs

def loadDataset(path=""):
	""" To load the dataSet"
		Parameter: The folder where the data files are stored
		Return: the dictionary with the data
	"""

	#Load the data
	prefs = {}
	count = 0
	for line in open(path+"Donor-Prod-Ratings2.csv"):
		line = line.replace('"', "")
		line = line.replace("\\","")
		(donor,prod,rating) = line.split(",")
		try:
			if float(rating) > 0.0:
				prefs.setdefault(donor,{})
				prefs[donor][prod] = float(rating)
		except ValueError:
			count+=1
			print "value error found! " + donor + prod + rating
		except KeyError:
			count +=1
			print "key error found! " + donor + " " + prod
	return prefs


from math import sqrt

#Returns a distance-base similarity score for person1 and person2

def sim_distance(prefs, person1, person2):
	#Get the list of shared_items
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	#if they have no rating in common, return 0
	if len(si) == 0: 
		return 0

	#Add up the squares of all differences
	sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])

	return 1 / (1 + sum_of_squares)


#Returns the Pearson correlation coefficient for p1 and p2 
def sim_pearson(prefs,p1,p2):
	#Get the list of mutually rated items
	si = {}
	for item in prefs[p1]:
		if item in prefs[p2]: 
			si[item] = 1

	#if they are no rating in common, return 0
	if len(si) == 0:
		return 0

	#sum calculations
	n = len(si)

	#sum of all preferences
	sum1 = sum([prefs[p1][it] for it in si])
	sum2 = sum([prefs[p2][it] for it in si])

	#Sum of the squares
	sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq = sum([pow(prefs[p2][it],2) for it in si])

	#Sum of the products
	pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

	#Calculate r (Pearson score)
	num = pSum - (sum1 * sum2/n)
	den = sqrt((sum1Sq - pow(sum1,2)/n) * (sum2Sq - pow(sum2,2)/n))
	if den == 0:
		return 0

	r = num/den

	return r

#Returns the best matches for person from the prefs dictionary
#Number of the results and similiraty function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_distance):
	scores = [(similarity(prefs,person,other),other)
				for other in prefs if other != person]
	scores.sort()
	scores.reverse()
	return scores[0:n]


#Gets recommendations for a person by using a weighted average
#of every other user's rankings

def getRecommendations(prefs,person,similarity=sim_distance):
	totals = {}
	simSums = {}

	for other in prefs:
		#don't compare me to myself
		if other == person:
			continue
		sim = similarity(prefs,person,other)

		#ignore scores of zero or lower
		if sim <= 0: 
			continue
		for item in prefs[other]:
			#only score books i haven't seen yet
			if item not in prefs[person] or prefs[person][item] == 0:
				#Similarity * score
				totals.setdefault(item,0)
				totals[item] += prefs[other][item] * sim
				#Sum of similarities
				simSums.setdefault(item,0)
				simSums[item] += sim

	#Create the normalized list
	rankings = [(total/simSums[item],item) for item,total in totals.items()]

	#Return the sorted list
	rankings.sort()
	rankings.reverse()
	return rankings



#Function to transform Person, item - > Item, person
def transformPrefs(prefs):
	results = {}
	for person in prefs:
		for item in prefs[person]:
			results.setdefault(item,{})

			#Flip item and person
			results[item][person] = prefs[person][item]
	return results





#Create a dictionary of items showing which other items they are most similar to.

def calculateSimilarItems(prefs,n=10):
	result = {}
	#Invert the preference matrix to be item-centric
	itemPrefs = transformPrefs(prefs)
	c=0
	for item in itemPrefs:
		#Status updates for large datasets
		c+=1
		#if c%100==0:
		#	print "%d / %d" % (c, len(itemPrefs))
		#Find the most similar items to this one
		scores = topMatches(itemPrefs,item,n=n,similarity=sim_distance)
		result[item] = scores
	return result

def getRecommendedItems(prefs, itemMatch, user):
	userRatings = prefs[user]
	scores = {}
	totalSim = {}
	#loop over items rated by this user
	for (item, rating) in userRatings.items():

		#Loop over items similar to this one
		for (similarity, item2) in itemMatch[item]:

			#Ignore if this user has already rated this item
			if item2 in userRatings:
				continue
			#Weighted sum of rating times similarity
			scores.setdefault(item2,0)
			scores[item2] += similarity * rating
			#Sum of all the similarities
			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity
	#Divide each total score by total weighting to get an average
	rankings=[]
	for item,score in scores.items():
		if totalSim[item] == 0:
			rankings.append((0,item))
		else:
			rankings.append((score/totalSim[item],item))
	#Return the rankings from highest to lowest
	rankings.sort()
	rankings.reverse()
	return rankings


def calculateSimilarDonors(prefs,n=10):
	result = {}
	#Invert the preference matrix to be item-centric
	donorPrefs = prefs
	c=0
	for donor in donorPrefs:
		#Status updates for large datasets
		c+=1
		if c%100==0:
			print "%d / %d" % (c, len(donorPrefs))
		#Find the most similar items to this one
		scores = topMatches(donorPrefs,donor,n=n,similarity=sim_distance)
		result[donor] = scores
	return result

def getRecommendedDonors(prefs, donorMatch, item):
	itemRatings = prefs[item]
	scores = {}
	totalSim = {}
	#loop over items rated by this user
	for (donor, rating) in itemRatings.items():
		#Loop over items similar to this one
		for (similarity, donor2) in donorMatch[donor]:
			#Ignore if this user has already rated this item
			if donor2 in itemRatings:
				continue
			#Weighted sum of rating times similarity
			scores.setdefault(donor2,0)
			scores[donor2] += similarity * rating
			#Sum of all the similarities
			totalSim.setdefault(donor2,0)
			totalSim[donor2]+=similarity
	#Divide each total score by total weighting to get an average
	rankings=[]
	for donor,score in scores.items():
		if totalSim[donor] == 0:
			rankings.append((0,donor))
		else:
			rankings.append((score/totalSim[donor],donor))
	#Return the rankings from highest to lowest
	rankings.sort()
	rankings.reverse()
	return rankings


def getJson(name):
    try:
		"""pref = loadDataset()
		result2 = calculateSimilarItems(pref)
		pref = loadDataset()
		don=loadDataset2()
		for d in don:
			result3 = getRecommendedItems(pref,result2,d)
			if("(0," not in str(result3[0:1])):
				print(str(d)+":"+str(result3[0:2]))"""
		pro=loadDataset3()
		pref = loadDataset()
		result4 = calculateSimilarDonors(pref)
		pref = loadDataset4()
		for p in pro:
			result5 = getRecommendedDonors(pref,result4,p)
			if("(0," not in str(result5[0:1]) and str(p)==name):
				j = json.dumps([str(p),result5[0:1]])
				return j
    except Exception as detail:
        print(detail)