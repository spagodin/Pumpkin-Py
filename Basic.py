
"""
Challenge 1: 

Given the dictionary "person"
Write a loop to print each key and value in a nice format
"""

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

def challenge_1():
    for key, value in person.items(): # the .items() method returns key-value pairs as touples
        print(f'{key}: {value}')

"""
Challenge 2

Given the dictionary "scores";
Write a program to find and print the player with the highest score:
"""

scores = {
    "player1": 25,
    "player2": 50,
    "player3": 142,
    "player4": 10
}

def challenge_2():
    player_name = ""
    highest_score = 0
    for player, score in scores.items():
        if score > highest_score:
            highest_score = score
            player_name = player
    
    print(f'{player_name} has the highest score with {highest_score} points')

"""
Challenge 3:
Given the dictionary fruits:
Write a program to count how many times each value appears in the dictionary
"""

fruits = {
    "apple": 3,
    "banana": 5,
    "cherry": 3,
    "date": 5
}

def challenge_3():
    value_counts = {}

    for value in fruits.values():
        if value in value_counts:
            value_counts[value] +=1
        else:
            value_counts[value] = 1
    
    for value, count in value_counts.items():
        print(f'{value} appears {count} times')
    
"""
Challenge 4:
Write a programe that takes a list of keys and creates a dictionary where each key has an initial value of 0:
"""

keys = ["x", "y", "z"]

def challenge_4():
    output = {}
    for k in keys:
        output[k] = 0
    print(output)

"""
Challenge 5: Given a nested dictionary, write a programe to calculate and print the average grade for each student
"""    

grades = {
    "Alice": {"Math": 85, "English":92},
    "Bob": {"Math": 78, "English": 80},
    "Charlie": {"Math": 95, "English": 85}
    }

def challenge_5():
    for student, courses in grades.items():
        average = sum(courses.values()) / len(courses)
        print(f"{student}'s grade is {average}")

"""
Challenge 6: Given two dictionaries, wrtie a program to create a new dictionary where
 - The values for matching keys are added together
 - Keys that appear in only on dictionary are included as-is
"""
dict1 = {"a":10,"b":20,"c":30}
dict2 = {"b":15, "c":5, "d":25}

def challenge_6():
    results = {}
    for k, v in dict1.items():
        # If key exists in results then add value to the key, else create new key and value
        if k in results:
            results[k] += v
        else:
            results[k] = v
    for k, v in dict2.items():
        if k in results:
            results[k] += v
        else:
            results[k] = v
    print(results)
     
"""
Alternative could import 'from collections import Counter

result = dict(Counter(dict1) + Counter(dict2))
print(result)
"""

"""
Challenge 7
Given a dictionary, write a program to create a new dictionary containing only items with a price greater than X
"""

prices = {
    "apple": 2.5,
    "banana": 1.2,
    "cherry": 3.0,
    "date": 1.8
}

def challenge_7(t):
    filtered = {}
    for k, v in prices.items():
        if v > t:
            filtered[k] = v
        else:
            pass
    print(filtered)

if __name__ == "__main__":

    challenge_7(2)