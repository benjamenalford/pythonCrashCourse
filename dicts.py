# dictionary
a_dict = {}

pies = []

pies.append({
            "name": "cherry pie",
            "price": 1.99,
            "ingredients": ["crust", "cherries"]
            })
pies.append({
            "name": "apple pie",
            "price": 4.99,
            "ingredients": ["crust", "apples", "TLC"]
            })
pies.append({
            "name": "pineapple pie",
            "price": 9.98,
            "ingredients": [" special crust", "pine", "apples", "ham"]
            })
total_price = 0.0

for pie in pies:
    print(pie["name"])
    print("    " + str(pie["price"]))
    total_price = total_price + pie["price"]  # pie_prices[1]
    for ing in pie["ingredients"]:
        print("    " + ing)

print(total_price)
