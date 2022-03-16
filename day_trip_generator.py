# Return after testing is done
# Use string temperlation instead of hard code


import random


destinations = ['Austin', 'Dallas', 'San Antonio', 'Houston']
def destination_name(destination_list):
    random_destination = random.choice(destination_list)
    print(random_destination)
    destination_name = (input(f"We have selected {random_destination} for your destination! Does this sound good? Enter y/n:"))
    y = True
    n = False
    while destination_name == "n":
     random_destination = random.choice(destination_list)
     destination_name = (input(f"We have selected {random_destination} for your destination! Does this sound good? Enter y/n:"))
destination_name(destinations)

restaurants = ['Taco Bell', 'McDonalds', 'Lubys', 'Churchs']
def restaurant_name(restaurant_list):
    random_restaurant = random.choice(restaurant_list)
    print(random_restaurant)
    restaurant_name = (input(f"We have selected {random_restaurant} for your restaurant! Does this sound good? Enter y/n:"))
    y = True
    n = False
    while restaurant_name == "n":
     random_restaurant = random.choice(restaurant_list)
     restaurant_name = (input(f"We have selected {random_restaurant} for your restaurant! Does this sound good? Enter y/n:"))
restaurant_name(restaurants)
   
transportations = ['Plane', 'Car', 'Train', 'Boat']
def transportation_name(transportation_list):
    random_transportation = random.choice(transportation_list)
    print(random_transportation)
    transportation_name = (input(f"We have selected {random_transportation} for your transportation! Does this sound good? Enter y/n:"))
    y = True
    n = False
    while transportation_name == "n":
     random_transportation = random.choice(transportation_list)
     transportation_name = (input(f"We have selected {random_transportation} for your transportation! Does this sound good? Enter y/n:"))
transportation_name(transportations)
       
entertainments = ['Movie', 'Play', 'Swimming', 'Hiking']
def entertainment_name(entertainment_list):
    random_entertainment = random.choice(entertainment_list)
    print(random_entertainment)
    entertainment_name = (input(f"We have selected {random_entertainment} for your entertainment! Does this sound good? Enter y/n:"))
    y = True
    n = False
    while entertainment_name == "n":
     random_entertainment = random.choice(entertainment_list)
     entertainment_name = (input(f"We have selected {random_entertainment} for your entertainment! Does this sound good? Enter y/n:"))
    entertainment_name(entertainments)
    sum_result = ((destinations) + (restaurants) + (transportations) + (entertainments))
entertainment_name(entertainments)
    




       
       




    



















