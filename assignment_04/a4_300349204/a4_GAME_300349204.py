# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     while len(deck)>0:
         other.append(deck.pop())
         if len(deck)>0:
             dealer.append(deck.pop())

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    for card in l:
        # Note, technically 10s are counted as 1s with this implementation, but this is not a
        # problem since 1s are represented as aces ('A')
        value=card[0]
        if value not in [c[0] for c in no_pairs]:
            no_pairs.append(card)
        else:
            for c in no_pairs:
                if c[0]==value:
                    no_pairs.remove(c)
                    break

    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    for card in deck:
        print(card,end=' ')
    print()

    
def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

    Precondition: n>=1
    '''

    prompt = "Give me an integer between 1 and " + str(n) + ": "
    user_input = input(prompt).strip()

    while not user_input.isdigit() or not 1 <= int(user_input) <= n:
        print("Invalid number. Please enter an integer between 1 and " + str(n) + ": ")
        user_input = input(prompt).strip()

    return int(user_input)


def ordinal_suffix(number: int) -> str:
    """
    Returns the ordinal suffix for a given number.

    :param number: The number for which to determine the ordinal suffix.
    :type number: int
    :return: The ordinal suffix as a string ("st", "nd", "rd", or "th").
    :rtype: str
    """
    last_two = number % 100

    if 11 <= last_two <= 13:
        return "th"

    suffixes = {1: "st", 2: "nd", 3: "rd"}
    return suffixes.get(number % 10, "th")

def player_turn(dealer: list[str], human: list[str]) -> tuple[list[str], list[str]]:
    '''
    This function implements the player's turn in the game.
    It takes the dealer's and human's decks as input and returns the updated decks after the player's turn.

    :param dealer: list of strings representing the dealer's deck
    :type dealer: list[str]
    :param human: list of strings representing the human's deck
    :type human: list[str]
    :return: a tuple containing the updated dealer's and human's decks
    :rtype: tuple[list[str], list[str]]
    '''
    print("***********************************************************")
    print("\nYour turn.\n")
    print("Your current deck of cards is:\n")

    print_deck(human)

    print(
        "\n"
        "I have " + str(len(dealer)) + " cards. If 1 stands for my first card and\n"
        + str(len(dealer)) + " for my last card, which of my cards would you like?"
    )

    user_input = get_valid_input(len(dealer))
    num_str = ordinal_suffix(user_input)

    print("You asked for my " + str(user_input) + num_str + " card.")
    card = dealer[user_input - 1]
    print("Here it is. It is " + card + ".\n")

    dealer.remove(card)
    human.append(card)

    print("With " + card + " added, your current deck of cards is:\n")
    print_deck(human)
    print("\nAnd after discarding pairs and shuffling, your deck is:\n")
    human = remove_pairs(human)
    print_deck(human)
    print("\n")

    return dealer, human

def comp_turn(dealer: list[str], human: list[str]) -> tuple[list[str], list[str]]:
    '''
    This function implements the computer's turn in the game.
    It takes the dealer's and human's decks as input and returns the updated decks after the computer's turn.

    :param dealer: list of strings representing the dealer's deck
    :type dealer: list[str]
    :param human: list of strings representing the human's deck
    :type human: list[str]
    :return: a tuple containing the updated dealer's and human's decks
    :rtype: tuple[list[str], list[str]]
    '''
    print("***********************************************************")
    print("My turn.\n")

    user_input = random.randint(1, len(human))
    card = human[user_input - 1]
    human.remove(card)
    dealer.append(card)

    num_str = ordinal_suffix(user_input)

    print("I took your " + str(user_input) + num_str + " card.")

    dealer = remove_pairs(dealer)

    return dealer, human

def play_game():
    '''()->None
    This function plays the game'''
    
    deck=make_deck()
    shuffle_deck(deck)
    tmp=deal_cards(deck)

    dealer=tmp[0]
    human=tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    dealer=remove_pairs(dealer)
    human=remove_pairs(human)

    while dealer and human:
        dealer, human = player_turn(dealer, human)

        if dealer and human:
            wait_for_player()
            dealer, human = comp_turn(dealer, human)
            wait_for_player()

    print("***********************************************************")
    if not human:
        print("Ups. You do not have any more cards\nCongratulations! You, Human, win")
    else:
        print("Ups. I do not have any more cards\nYou lost! I, Robot, win")
	 

# main
play_game()
