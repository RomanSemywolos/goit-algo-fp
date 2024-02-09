import random

budget = random.randrange(100, 500)
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget, items):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = {}
    remaining_budget = budget

    for item_name, item_info in sorted_items:
        while remaining_budget >= item_info['cost']:
            if item_name not in selected_items:
                selected_items[item_name] = 0
            selected_items[item_name] += 1
            remaining_budget -= item_info['cost']

    return selected_items


def dynamic_programming(budget, items):
    num_items = len(items)
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        item_name, item_info = list(items.items())[i - 1]
        for j in range(budget + 1):
            if item_info['cost'] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - item_info['cost']] + item_info['calories'])

    selected_items = {}
    i, j = num_items, budget

    while i > 0 and j > 0:
        item_name, item_info = list(items.items())[i - 1]
        if dp_table[i][j] != dp_table[i - 1][j]:
            if item_name not in selected_items:
                selected_items[item_name] = 0
            selected_items[item_name] += 1
            j -= item_info['cost']
        else:
            i -= 1
    return selected_items


print(budget)
print(greedy_algorithm(budget, items))
print(dynamic_programming(budget, items))