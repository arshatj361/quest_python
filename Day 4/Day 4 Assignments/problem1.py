'''
User gives the data like this:
kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
You have to separate the states and store in the list states[] and also the seperated capitals must be stored in capitals[]
'''



def separate_states_and_capitals(*pairs):
    states = []
    capitals = []
    
    for pair in pairs:
        state, capital = pair.split('-')
        states.append(state)
        capitals.append(capital)
    
    return states, capitals


input_pairs = [
    "kerala-tiruvanantapuram",
    "karnataka-bengaluru",
    "tamilnadu-chennai"
]

states, capitals = separate_states_and_capitals(*input_pairs)

# Print the results
print("States:", states)
print("Capitals:", capitals)