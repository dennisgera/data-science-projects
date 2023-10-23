# write a restaurante recommendation program to the user based on the information on restaurants_data.py
# the program should ask the user what type of food he would like to eat and show the available restautrants
#
# Example:
# What type of food would you like to eat?
# > mexican
# Here are your restaurant choices:
# 1. Cancun
# 2. The Whole Tamale
# 3. Pedro's

# What type of food would you like to eat?
# > chinese
# Here are your restaurant choices:
# 1. Beijing Express
# 2. Dragon's Tail
# 3. Super Wonton Express

from restaurant_data import restaurant_data

def main():
    # get the type of food from the user
    food_type = input("What type of food would you like to eat?\n> ")
    # print the restaurants that match the type of food
    print(f"Here are your restaurant choices:")
    for i in range(len(restaurant_data)):
        if restaurant_data[i][0] == food_type:
            print(f"{i+1}. {restaurant_data[i][1]}")

if __name__ == "__main__":
    main()