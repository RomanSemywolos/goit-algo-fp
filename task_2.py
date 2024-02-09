import turtle

def draw_pifagorean_tree(branch_length, t, angle, level):
    if level == 0:
        return
    else:
        t.forward(branch_length)
        t.right(angle)
        draw_pifagorean_tree(0.7 * branch_length, t, angle, level - 1)
        t.left(2 * angle)
        draw_pifagorean_tree(0.7 * branch_length, t, angle, level - 1)
        t.right(angle)
        t.backward(branch_length)

def main():
    # Рівень рекурсії
    rec = int(input("Введіть рівень рекурсії для фрактала 'оголене' дерево Піфагора: "))

    # Налаштуємо вікно Turtle
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("green")
    turtle.width(2)
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()

    # Викликаємо функцію для малювання фрактала
    draw_pifagorean_tree(100, turtle, 30, rec)

    turtle.exitonclick()

if __name__ == "__main__":
    main()