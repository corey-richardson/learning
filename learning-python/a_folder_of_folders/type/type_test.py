def set_list():
    global strings_to_choose_from
    strings_to_choose_from = [\
    "The quick brown fox jumped over the lazy dog",\
    "A horse was sat at home watching MTV",\
    "hello WORLD! my first program :)",\
    "Tuesday the 13th of December 2022",\
    "'RED' is a bigger number than 'BLUE'",\
    "You think I ain't worth a dollar, but I feel like a Millionaire",\
    "hey, all right! It's Kip Kasper, KLONE Radio",\
    "How's your drive time commute? I need a saga",\
    "These aren't the droids you're looking for",\
    "You don't find your way, the way finds you",\
    "Kalopsia: Bye, bye, black baloon",\
    "Gossips, frauds and snakes; they're just our best fairweather friends",\
    "Ho, Ho, Ho, Merry Christmas!",\
    "We're painted as monsters. Borracho, cansado",\
    "Hippopotomonstrosesquipedaliaphobia",\
    "Bye-bye Shanghai, I've become a butterfly!",\
    "I wanna be your vacuum cleaner...",\
    "Sometimes you break a finger on the upper hand",\
    "Give me the flammable light, cold as a match",\
    "Hello, I've waited here for you Everlong",\
    "The compartmentalised thoughts in the back corner of the drawer.",\
    "Who should we believe? Who's to believe?",\
    "Keep you in the dark, you know they all pretend",\
    "The faster the world spins, the shorter the lights will glow",\
    "Not everything that goes around comes back around you know",\
    "Holding on too long is just the fear of letting go",\
    "One thing that is clear, it's all downhill from here",\
    "I'll be massive conquistador",\
    "The blue pill opens your eyes, is there a better way?",\
    "A new religion prescribed to those without a faith",\
    "Magma, fire bagwan, the all, the one and the none",\
    "There's no magic bullet, no cure for pain",\
    "What's done is done, till you do it again",\
    "Save me from the Villians of Circumstance",\
    "MATLAB for Data Processing and Visualisation",\
    "SELECT * FROM data WHERE variable matches expression",\
    "0118 999 88199 911 9725 3",\
    ]

def main():
    set_list()
    scores = [] # initialise empty list
    for i in range(5): # repeat 5 times
        # pick a random string from the list, then remove that string from the choices
        compare_against = generate_string()
        time_taken, user_string = user_type(compare_against) 
        ratio = compare_strings(compare_against, user_string)
        score = get_score(ratio, time_taken, len(compare_against))
        scores.append(score) # add score for that string into a list
    mean = (sum(scores) / len(scores))*100 # calculate the mean score timesed by 100
    
    print("You had a score of %i!" % mean)
      
def generate_string():
    from random import choice
    compare_against = choice(strings_to_choose_from)
    strings_to_choose_from.remove(compare_against) # remove selected string from list
    return compare_against
    
def user_type(compare_against):
    input("\nPress enter to begin... ")
    print(compare_against)
    from time import perf_counter
    start = perf_counter() # start timer
    user_string = input()
    end = perf_counter() # end timer
    return (end - start), user_string

# get similiarity ratio of two strings 
def compare_strings(compare_against, user_string):
    from difflib import SequenceMatcher
    ratio = SequenceMatcher(None, compare_against, user_string).ratio()
    if int(ratio) == 1: print("Perfect match!")
    return ratio

# calculate score
def get_score(ratio, time_taken, length_of_string):
    try:
        return ( ratio * (1 / time_taken) ) * length_of_string
    except ZeroDivisionError: # if time taken = 0 seconds (impossible)
        return ratio * length_of_string

if __name__ == "__main__":
    main()
    

# while True:
#     try:   
#         compare_against = generate_string()
#         set_list
#     except IndexError:
#         set_list()
#     except NameError:
#         set_list()
#     except KeyboardInterrupt:
#         string_analysis()
#         import sys
#         sys.exit()