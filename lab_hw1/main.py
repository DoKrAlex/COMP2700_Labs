# Problem 1
from copy import deepcopy

def power_set(S):
    """
    Finds all the subsets of S recursively.

    Args:
    S: A list of elements.

    Returns:
    list: A list of subsets as lists.

    Hint: use deepcopy() for copying lists.
    """
    if len(S) == 0:
        return [[]]
    else:
        S_copy = deepcopy(S)
        first = S_copy.pop(0)
        rest = power_set(S_copy)
        rest_copy = deepcopy(rest)
        for i in range(len(rest)):
            rest[i].append(first)
        return rest + rest_copy


# Test case
S = ["Torchic", "Rowlet", "Piplup"]
print("S:")
print(str(S))

print("\npower_set(S): ")
import pprint
pprint.pprint(power_set(S))


# Problem 2
from copy import deepcopy
E = [[1, 36, 5], 
     [2, 264, 9], 
     [3, 188, 6], 
     [4, 203, 8], 
     [5, 104, 8], 
     [6, 7, 6],
     [7, 92, 2], 
     [8, 65, 8], 
     [9, 25, 3], 
     [10, 170, 6], 
     [11, 80, 7], 
     [12, 22, 4]]

def power_set(E):
    new_set = [[]]
    for i in E:
        for j in new_set[:]:
            new_set += [j+ [i]]
    return new_set
    #return empty list if mass limit is 0 or E is empty


def find_optimal_subset(m):
    #subset=[], total mass=0, total value rating=0
	#as index 0 should contain a subset of E, we have an empty list for that
	#total mass and value rating are initialized to 0
    apc = power_set(E)
    mass_of_combination = 0
    full_mass_list = []
    value_of_combination = 0
    full_value_list = []
    tab=0

    for i in range(len(apc)): 
        for j in range(len(apc[i])):
            mass_of_combination += apc[i][j][1]
            value_of_combination += apc[i][j][2] 
            #if total mass of result is less than mass limit m
			#and total mass will not exceed mass limit after inserting row(set)
			#insert row to subset and increase the total mass and value rating accordingly
        tab+=1
        #if our subset has already reached to its mass limit
		#we will check if we can replace some set from our subset with a better set
		#visit each row of result(not E)
        full_mass_list.append(mass_of_combination)
        full_value_list.append(value_of_combination) 
        mass_of_combination = 0
        value_of_combination = 0
    r = 0

    while r < len(full_mass_list):
        if full_mass_list[r] > m: #if we find a set with more value rating or less mass, we will replace it
            del full_value_list[r]
            del full_mass_list[r]
            del apc[r]
        else:  
            r += 1
    max_value = full_value_list.index(max(full_value_list))
    return apc[max_value]
print(find_optimal_subset(700))


#Question 3
#putting table data as lists manually
ids= list(range(1,13))

experiment = list()
experiment.append("How rats behave in the absence of oxygen")
experiment.append("Solar radiation study")
experiment.append("X-ray observatory")
experiment.append("Solar flare observation device")
experiment.append("Low - gravity bear wrestling gear")
experiment.append("CLASSIFIED TOP SECRET")
experiment.append("Solid propellant behavior in microgravity")
experiment.append("Cloaking field generator")
experiment.append("Prototype handheld stun phaser")
experiment.append("Laminar fluid flow study")
experiment.append("Low Earth orbit race of African vs. European swallows")
experiment.append("Hyper- efficient RCS thruster")

mass = [36,264,188,203,104,7,92,65,25,170,80,22]
value = [5,9,6,8,8,6,2,8,3,6,7,4]

####################################

##Start####################

#Powerset, provides set of all possible combinations
def powerset(ids):
    res = [[]]
    for num in ids:
        newset = [r+[num] for r in res]
        res.extend(newset)
    return res

#All candidates consists of all combinations possible of IDs
allCandidates = powerset(ids)
finalIds=[]
maxValue = -1
finalMass=-1


for candidateList in allCandidates:
    #Retriving mass and value, by using id as an Index
    massById =[]
    valueById =[]
    for idx in candidateList:
        massById.append(mass[idx-1])
        valueById.append(value[idx-1])

    #If total mass doesnt exceeds 700, then its a prospect
    totalMass = sum(massById)
    if totalMass <= 700:
        totalValue = sum(valueById)
        #if it's value is greater than any occured before
        if totalValue > maxValue:
            maxValue = totalValue
            finalIds=candidateList
            finalMass=totalMass

print('Ids of Best Value - Weight Combo',finalIds)
print('Summing up a value of ',maxValue)
print('Total Mass ', finalMass)


#Question 4
for e in range(rows):
    E += [([randint(1,100)] * cols)]
start_time = process_time() 