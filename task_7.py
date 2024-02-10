import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Словник можливих випадків для кожної суми
    sum_counts = {sum_value: 0 for sum_value in range(2, 13)}

    # Кидки
    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[roll_sum] += 1

    # Ймовірності
    probabilities = {sum_value: count / num_rolls for sum_value, count in sum_counts.items()}

    # Результат у консоль
    print(f"\n{num_rolls} кидків")
    print("Сума\tІмовірність")
    for sum_value, probability in probabilities.items():
        print(f"{sum_value}\t{probability:.2%}")

    # Результат у графік
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума кубиків')
    plt.ylabel('Імовірність')
    plt.title(f'Імовірності сум (2к6) (Метод Монте-Карло, {num_rolls} кидків)')
    plt.xticks(range(2, 13))
    plt.show()


if __name__ == "__main__":
    simulate_dice_rolls(100)
    simulate_dice_rolls(1000)
    simulate_dice_rolls(10000)
    simulate_dice_rolls(100000)
