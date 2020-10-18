from DtreeMethods import DtreeMethods


# data must be in oder from crust size, shape, filling size and class
pie_data = [
    ["big", "circle", "small", "pos"],
    ["small", "circle", "small", "pos"],
    ["big", "square", "small", "neg"],
    ["big", "triangle", "small", "neg"],
    ["big", "square", "big", "pos"],
    ["small", "square", "small", "neg"],
    ["small", "square", "big", "pos"],
    ["big", "circle", "big", "pos"],
]
best_attribute = DtreeMethods.find_best_attribute(pie_data)
print("best attribute to split on:", best_attribute)
