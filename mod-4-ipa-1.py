'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    list_from_members = social_graph.keys()
    
    
    def follower(from_member):
        
        from_member_following_list = social_graph[from_member]["following"]
    
        if to_member in from_member_following_list:
            return True
        else:
            return False
        
    def followed_by(to_member):
        
        to_member_following_list = social_graph[to_member]["following"]
        
        if from_member in to_member_following_list:
            return True
        
        else:
            return False
    
    if from_member in list_from_members and to_member in list_from_members:
        
        if follower(from_member) == True and followed_by(to_member) == True:
            return "friends"
    
        elif follower(from_member) == True:
            return "follower"
    
        elif followed_by(to_member):
            return "followed by"
        
        else:
            return "no relationship"
            
    elif from_member in list_from_members:
        
        if follower(from_member) == True:
            return "follower"
        
        else:
            return "no relationship"
            
    elif to_member in list_from_members:
        
        if followed_by(to_member) == True:
            return "followed by"
        
        else:
            return "no relationship"
            
    else:
        return None


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    dms = len(board[0]) - 1 #dimensions

    
    h_check = [len(set(row)) for row in board]
    v_check = [len(set(col)) for col in zip(*board)]
    d1_check = len(set([board[i][i] for i,v in enumerate(board)]))
    d2_check = len(set([board[dms-i][i] for i,v in enumerate(board)]))
    
    
    if 1 in h_check:
        return(board[h_check.index(1)][0])
            
    elif 1 in v_check:
        return(board[0][v_check.index(1)])
    
    elif 1 == d1_check:
        return(board[0][0])
                     
    elif 1 == d2_check:
        return(board[dms][dms])
        
    else:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    keys = list(route_map.keys()) # to and from point of one leg of the trip
    from_place = [keys[i][0] for i,v in enumerate(keys)] # origin stop list
    to_place = [keys[i][1] for i,v in enumerate (keys)] # destination stop list
    
    dict_from_index = from_place.index(first_stop) 
    dict_to_index = to_place.index(second_stop) 
    
   
    total_time = route_map[keys[dict_from_index]]["travel_time_mins"] # travel time of first leg
    
    number_of_stops = len(keys)-1
    index = dict_from_index 
    
    if dict_from_index == dict_to_index: # if origin and destination belong to the same leg of a trip
        return total_time
    
    else:
        for i in range(number_of_stops):
            stop = keys[index][1] 
            index = from_place.index(stop) 
            next_leg = keys[index] # next leg of trip
        
            total_time += route_map[next_leg]["travel_time_mins"]
            
            if index == dict_to_index:
                return total_time
                break