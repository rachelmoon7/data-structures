"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    open_name = open(filename)

    for line in open_name:
        bio = line.split('|')
        species.add(bio[1])

    open_name.close()
    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

  

    open_name = open(filename)
    villagers = []
    for line in open_name:
        bio = line.split('|')
        if bio[1] == search_string:
            villagers.append(bio[0])

    open_name.close()

    return sorted(villagers)



def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
   
    data = open(filename)
    # hobbies = []
    
    # for line in data:
    #   bio = line.split('|')
    #   hobbies.append(bio[3])

    # set_hobbies = set(hobbies)
    # print(set_hobbies)
    nature =[]
    education = []
    fitness = []
    fashion = []
    music = []
    play = []

    for line in data:
        bio = line.split('|')
        hobby = bio[3]
        name = bio[0]
        if hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
              education.append(name)
        elif hobby == "Fitness":
              fitness.append(name)
        elif hobby == "Fashion":
              fashion.append(name)
        elif hobby == "Music":
              music.append(name)
        elif hobby == "Play":
             play.append(name)                          
        
    

    return [[nature], [education], [fitness], [fashion], [music], [play]]



def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    open_name = open(filename)

    #read each line of data
    for line in open_name:
        #return a list of name, species, personality, hobby, and motto 
        bio = line.split('|')
        #return a tuple contaning elements of bio list
        tups_of_info = tuple(bio)
        all_data.append(tups_of_info)

    return all_data




def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    open_name = open(filename)

    for line in open_name:
        bio = line.split('|')
        if villager_name == bio[0]:
            return bio[4]
        else: 
            return None
    



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    personality = []
    names_personality = None
    open_name = open(filename)

    #iterate through each line of data
    for line in open_name:
        #return list of name, species, personality, hobby, mott
        bio = line.split('|')
        #if name matches argument villager_name
        if villager_name == bio[0]:
            #set variable names_personality to the villager_name's personality
            names_personality = bio[2]
        #if bio[2] which is personality matches names_persanlity, push name into personality set
        if bio[2] == names_personality:
            personality.append(bio[0])
    return sorted(set(personality))

print(find_likeminded_villagers("villagers.csv", "Pango"))