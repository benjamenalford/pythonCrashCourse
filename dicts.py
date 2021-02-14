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
pies.append({
    "name": "plain",
    "price": .99,
    "ingredients": []
})
total_price = 0.0

for pie in pies:
    print(pie["name"])
    print("    " + str(pie["price"]))
    total_price = total_price + pie["price"]
    if (len(pie["ingredients"]) > 0):  # pie_prices[1]
        for ing in pie["ingredients"]:
            print("    " + ing)
    else:
        print("    i have none")
print(total_price)
