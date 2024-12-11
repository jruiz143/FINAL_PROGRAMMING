#FINAL EXAM QUESTION 2
#CREATE A FUNCTION CALLED COUNT_FREQUENCIES THAT WILL COUNT HOW MANY OCCURENCES 
#OF A WORD APPEARS IN A STRING
#DON'T USE THE COUNT METHOD IN THE LIST CLASS.PLEASE USE A DICTIONARY

def main(): 
    input_strings = ["LATTE", "COFFEE", "LATTE", "EXPRESSO", "CORTADO", "COFFEE", "COFFEE"]
    frequency_count = count_frequencies(input_strings)
    print("Frequency Count:", frequency_count) #DISPLAY RESULT


def count_frequencies(input_list):
    frequency_dict = {} #CREATE EMPTY DICT TO STORE WORD FREQUENCIES
    
    # LOOP THROUGH EACH WORD IN THE LIST
    for word in input_list:
        if word in frequency_dict: #CHECK IF WORD IS FOUND IN THE LIST
            current_count = frequency_dict[word] #GET CURRENT COUNT OF HOW MANY TIMES WORD APPEAR
            new_count = current_count + 1   #INCREASE COUNT BY ONE
            frequency_dict[word] = new_count #DICTIONARY IS UPDATED TO NEW WORD COUNT 
        else:
            frequency_dict[word] = 1 #KEEPS SINGLE COUNT IF ONLY ONE IS FOUND
    
    # RETURN DICTIONARY
    return frequency_dict

#CALL MAIN
if __name__ == "__main__":
    main()