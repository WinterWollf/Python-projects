def wczytaj_dane():
    file_name = "data.txt"
    list_1 = []
    list_2 = []

    with open(file_name, 'r') as file:
        for line in file:
            date = line.strip().split(',')
            if len(date) == 2:
                list_1.append(int(date[0]))
                list_2.append(int(date[1]))

    return list_1, list_2


# Lagrange interpolation #
def lagrange_interpolation(x, x_values, y_values):
    n = len(x_values)
    result = 0

    for i in range(0, n):
        y_i = y_values[i]
        for j in range(0, n):
            if i != j:
                y_i = y_i * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += y_i

    return result


# Main #
x_val = [1, 2, 3, 4]
y_val = [1, 4, 9, 16]

# DATE #
l_1, l_2 = wczytaj_dane()
print("List 1:", l_1)
print("List 2:", l_2)

number = float(input("Please enter a number: "))
print(f"The interpolation of a point {number} is {lagrange_interpolation(number, x_val, y_val)}")