# Course: ITI 1120
# Assignment: 5
# Geraghty, Patrick
# 300349204

import random

def find_id_index(ids: list[int], target: int) -> int:
    """
    Binary search to find the index of a target ID in a sorted list of IDs.

    :param ids: List of sorted user IDs
    :type ids: list[int]
    :param target: Target user ID to find
    :type target: int
    :return: Index of the target ID if found, otherwise -1
    :rtype: int
    """
    left, right = 0, len(ids) - 1
    while left <= right:
        mid = (left + right) // 2
        if ids[mid] == target:
            return mid
        elif ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_user_index(network: list[tuple[int, list[int]]], user_id: int) -> int:
    """
    Binary search to find the index of a user in the network based on user ID.

    :param network: List of tuples where each tuple contains a user ID and a list of friends
    :type network: list[tuple[int, list[int]]]
    :param user_id: User ID to find
    :type user_id: int
    :return: Index of the user in the network if found, otherwise -1
    :rtype: int
    """
    left, right = 0, len(network) - 1
    while left <= right:
        mid = (left + right) // 2
        if network[mid][0] == user_id:
            return mid
        elif network[mid][0] < user_id:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friends is sorted).
    '''
    # Assuming we can't use sets, dictionaries, or maps (what a pain)
    # However, we will use binary search for fun (surely there isn't a restriction on what I can code?)
    with open(file_name) as file:
        lines = file.read().splitlines()

    edges = []
    all_ids = []

    # Collect all edges and user IDs from each line after user count
    for line in lines[1:]:
        values = line.split()
        user_id = int(values[0])
        friend_id = int(values[1])

        edges.append((user_id, friend_id))
        all_ids.append(user_id)
        all_ids.append(friend_id)

    all_ids.sort()

    # Create de-duplicated list of user IDs
    ids = []
    for user_id in all_ids:
        if len(ids) == 0 or user_id != ids[-1]:     # Only need to check last element since the list is sorted
            ids.append(user_id)

    # Initialize dummy network
    network = []
    for user_id in ids:
        network.append((user_id, []))

    # Populate the network with friends
    for user_id, friend_id in edges:
        user_index = find_id_index(ids, user_id)
        friend_index = find_id_index(ids, friend_id)

        network[user_index][1].append(friend_id)
        network[friend_index][1].append(user_id)

    for user_id, friends in network:
        friends.sort()

    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]

    # Get the friends lists for user1 and user2
    user1_index = find_user_index(network, user1)
    user2_index = find_user_index(network, user2)

    friends1 = network[user1_index][1]
    friends2 = network[user2_index][1]

    # Use two pointers to find common friends
    i, j = 0, 0
    while i < len(friends1) and j < len(friends2):
        if friends1[i] == friends2[j]:
            common.append(friends1[i])
            i += 1
            j += 1
        elif friends1[i] < friends2[j]:
            i += 1
        else:
            j += 1

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID.
    '''

    # Get the friends of the user
    user_index = find_user_index(network, user)
    user_friends = network[user_index][1]

    # Determine the best match without sets or dictionaries :(
    best_match = None
    max_common_friends = 0

    # Also assuming enumerate is not allowed
    for other_user_index in range(len(network)):
        other_user_id = network[other_user_index][0]

        if other_user_id == user or other_user_id in user_friends:
            continue  # Skip the user themselves and their friends

        other_user_friends = network[other_user_index][1]

        # Run two pointers to count common friends
        i = 0
        j = 0
        common_count = 0

        while i < len(user_friends) and j < len(other_user_friends):
            if user_friends[i] == other_user_friends[j]:
                common_count += 1
                i += 1
                j += 1
            elif user_friends[i] < other_user_friends[j]:
                i += 1
            else:
                j += 1

        if common_count > max_common_friends:
            max_common_friends = common_count
            best_match = other_user_id

    return best_match

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    count = 0
    for user_id, friends in network:
        if len(friends) >= k:
            count += 1
    return count
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    max_friends = 0
    for user_id, friends in network:
        if len(friends) > max_friends:
            max_friends = len(friends)
    return max_friends
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    for user_id, friends in network:
        if len(friends) == maximum_num_friends(network):
            max_friends.append(user_id)

    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network
    '''
    total_friends = 0
    for user_id, friends in network:
        total_friends += len(friends)
    return total_friends / len(network)
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    for user_id, friends in network:
        if len(friends) == len(network) - 1:
            return True
    return False


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    uid = None
    ids = [user_id for user_id, _ in network]
    while uid == None:
        uid = input("Enter an integer for a user ID: ").strip()
        if not uid.isdigit():
            print("That was not an integer. Please try again.")
            uid = None
            continue
        uid = int(uid)
        if uid not in ids:
            print("That user ID does not exist. Try again.")
            uid = None
    return uid
    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
