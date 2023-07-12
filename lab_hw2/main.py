# 1. defining function is_function
def is_function(f,A,B):
    # extracting domain of f in sorted order using set comprehenstion
    domain = {val[0] for val in f}
    # extracting range of f in sorted order using set comprehenstion
    rnge = {val[1] for val in f}

    # checking domain set is subset of A and rnge is subset of B
    # using issubset method of sets in python
    return domain.issubset(A) and rnge.issubset(B)

# 2. defining function_range
def function_range(f,A,B):
    # checking if f is a function of A and B
    if is_function(f,A,B):
        # using set comprehenstion to extract range and convert to list
        return list({val[1] for val in f})
    else:
        return None

# 3. defining function is_one_to_one
def is_one_to_one(f,A,B):
    # checking if f is a function of A and B
    if not is_function(f,A,B):
        return None

    # creating a dictonary to store all values of B w.r.t A
    relations = {val[0]:[] for val in f}
    # looping for every pair in f
    for x,y in f:
        # appending y to x list
        relations[x].append(y)

    # iterating through each pair in relations, and checking if more than one
    # unique relation exist, using set function to find unique values
    for key in relations:
        if len(set(relations[key]))>1:
            return False

    # otherwise return True
    return True

# 4. defining function is_onto
def is_onto(f,A,B):
    # checking if f is a function of A and B
    if not is_function(f,A,B):
        return None

    # fetching range of f
    rnge = function_range(f,A,B)

    # if rnge of f not equal B, means there is no relation from domain for every value in B
    return rnge==B

# Testing
if name=='main':
    # defining A,B and f
    A = [1,2,3]
    B = [4,5]
    f = [[1,4],[2,5],[3,4]]

    # displaying results
    print("1. is_function(f,A,B):",is_function(f,A,B))
    print("2. function_range(f,A,B):",function_range(f,A,B))
    print("3. is_one_to_one(f,A,B):",is_one_to_one(f,A,B))
    print("4. is_onto(f,A,B):",is_onto(f,A,B))
    

# 5. defining function inverse
def inverse(f,A,B):
    if is_function(f,A,B)== True and is_one_to_one(f,A,B)== True and is_onto(f,A,B)==True: #check if it is a function and both onetoone and onto(bijective),
        #then its has an inverse...
        temp = ''
        for i in range(len(f)):
            for j in range(len(f)):
            temp = f[i][j]#swapping the positions of domain and range.
            f[i][j] = f[i][1]
            f[i][1] = temp

            i=i+1
            temp = f[i][j]#swapping the positions of domain and range.
            f[i][j] = f[i][1]
            f[i][1] = temp

            i=i+1
            temp = f[i][j]#swapping the positions of domain and range.
            f[i][j] = f[i][1]
            f[i][1] = temp
            return f
        return None
    A = [1,2,3]
    B = [4,5,6]
    f = [[1,4],
    [2,5],
    [3,6]]
    print "-------------q4------------------"
    print inverse(f,A,B)
    print "---------------------------------\n"