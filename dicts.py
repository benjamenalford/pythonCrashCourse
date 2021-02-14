# Variables
a_number = 0  # assumes integer / whole number
b_number = 0.0  # force to float number ( has decimal )
some_test = "text text text"

# data structures
list_of_items = []
list_of_items_2 = [1, 2, 3, 4]
list_of_numbers = [a_number, b_number]
list_of_items = ["cherry", "apple", "bacon"]  # anything

# dictionary
a_dict = {}
a_dict_2 = {"pie": "cherry"}
a_dict['pie'] = "cherry"

pies = []
pie_prices = []
pie_ingredients = []

pies.append("cherry")
pie_prices.append(1.99)
pie_ingredients.append(["crust", "cherries"])

pies.append("apple")
pie_prices.append(4.99)
pie_ingredients.append(["crust", "apples"])

# print(pies)
# print(pie_prices)
# print(pie_ingredients)
total_price = 0.0
# for i in range(0, len(pies)):
#     total_price = total_price + pie_prices[i]
#     print(pies[i])
#     print(pie_ingredients[i])


for pie in pies:
    print(pie)
    print(pie_ingredients[pies.index(pie)])
    total_price = total_price + pie_prices[pies.index(pie)]  # pie_prices[1]

print(total_price)
