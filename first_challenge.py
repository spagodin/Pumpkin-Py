import pprint
"""
Sample Data
"""

# A list of student names
students = ["Alice","Bob","Charlie","Diana"]

# A ditionary of student grades
grades = {
    "Alice": {"Math": 85, "Science": 92},
    "Bob": {"Math": 78, "Science": 80},
    "Charlie": {"Math": 88, "Science": 85},
    "Diana": {"Math": 95, "Science": 99}
}

# A list of product dictionaries
products = [
    {"name": "Laptop", "price": 1000, "stock": 5},
    {"name": "Smartphone", "price": 500, "stock": 10},
    {"name": "Headphones", "price": 50, "stock": 100}
]

items = ["apple", "banana", "apple", "orange", "banana", "banana"]

# 1. Write a loop to print each student's name in uppercase
def student_upper():
    for name in students:
        print(name.upper())

# 2. Iterate over the grades dictionary and print each student's name and their grades
def student_grades():
    for name, scores in grades.items():
        print(f'{name}: {scores}')

# 3. Write a loop to calculate and print the average grade for each student
def grade_average():
    for name, scores in grades.items():
        average = sum(scores.values()) / len(scores)
        print(f'{name} has an average of {average}')

# 4. Iterate over the products list and print the names of products that cost more than $100
def filter_products():
    for product in products:
        if product['price'] > 100:
            print(product['name'])
        

# 5. Write a function that takes a list of items and returns a dictionary counting how many times each item appears
def count_items():
    summary = {}
    for item in items:
        if item in summary:
            summary[item] +=1
        else: 
            summary[item] = 1
    print(summary)


# 6. Add a "Total" key to each student's dictionary in grades that contains their total score (sum of all grades)
def add_total():
    for name, score in grades.items():
        total = sum(score.values())
        score['Total'] = total
    pprint.pprint(grades)

# 7. Write a function that takes a list of student names and their corresponding grades, and returns a dictionary combining them
names = ["Eve", "Frank"]
scores = [{"Math": 82, "Science": 89}, {"Math": 76, "Science": 81}]
combined = {}
def combiner():
    for i in range(len(names)):
        combined[names[i]] = scores[i]
    pprint.pprint(combined)

# 8. Iterate through the products list to find and print the name of the product with the highest price.
def find_max():
    max_price = 0
    max_product = ""
    for product in products:
        if product['price'] > max_price:
            max_price = product['price']
            max_product = product['name']
        else:
            pass
    print(f"The most expensive item is {max_product} with a {max_price} as it's maximum price")



if __name__ == "__main__":
    print("These are my solutions(output)\n")
    print("#1. Student names to upper:\n")
    student_upper()
    print("\n#2. Students with their grades by course:\n")
    student_grades()
    print("\n#3. Student averages:\n")
    grade_average()
    print("\n#4. Filtered Products:\n")
    filter_products()
    print("\n#5. Summary of items:\n")
    count_items()
    print("\n#6. Totals Added:\n")
    add_total()
    print("\n#7. Combined Names and Scores from two lists\n")
    combiner()
    print("\n#8. Max Priced Item\n")
    find_max()