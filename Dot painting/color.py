import colorgram

number_of_colors = 20
colors = colorgram.extract("painting.jpg", number_of_colors)
rbg_colors = []

for i in range(0, number_of_colors):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    rbg_colors.append((r,g,b))


def color_pallet():
    return rbg_colors
