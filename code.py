# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)

# Find data type of the file
print(type(data))

# In which city, and at which venue the match was played and where was it played ?
print(data['info']['city'])
print(data['info']['venue'])

# Which are all the teams that played in the tournament ? How many teams participated in total?
print(data['info']['teams'])
print(len(data['info']['teams']))

# Which team won the toss and what was the decision of toss winner ?
print((data['info']['toss']['winner']),"Decision:",(data['info']['toss']['decision']))

# Find the first bowler and first batsman who played the first ball of the first inning
#print(data['innings']['1st innings'](1))


# How many deliveries were delivered in first inning ?


# How many deliveries were delivered in second inning ?


# Which team won and how ?



