from DtreeMethods import DtreeMethods
from enum import Enum


class PIE_COLUMNS(Enum):
    ID = 0
    CRUST_SIZE = 1
    SHAPE = 2
    FILLING_SIZE = 3
    CLASS = 4

# data must be in order from crust size, shape, filling size and class, according to the Enum
pie_data = [
    ["1", "big", "circle", "small", "pos"],
    ["2", "small", "circle", "small", "pos"],
    ["3", "big", "square", "small", "neg"],
    ["4", "big", "triangle", "small", "neg"],
    ["5", "big", "square", "big", "pos"],
    ["6", "small", "square", "small", "neg"],
    ["7", "small", "square", "big", "pos"],
    ["8", "big", "circle", "big", "pos"],
]


best_pie_attribute_data = DtreeMethods.find_best_attribute(pie_data)
print("best attribute in pies domain to split on:", PIE_COLUMNS(best_pie_attribute_data[0]).name, "\n")
print("pie domain attribute value entropies:")
for attribute_value_tuple in best_pie_attribute_data[1]:
    print(PIE_COLUMNS(attribute_value_tuple[0]).name, attribute_value_tuple[1],
          best_pie_attribute_data[1][attribute_value_tuple])
print()
print("pie domain attribute entropies:")
for attribute in best_pie_attribute_data[2]:
    print(PIE_COLUMNS(attribute).name, best_pie_attribute_data[2][attribute])
print()
print("pie domain attribute information gains:")
for attribute in best_pie_attribute_data[3]:
    print(PIE_COLUMNS(attribute).name, best_pie_attribute_data[3][attribute])
print()


class CHESS_COLUMNS(Enum):
    ID = 0
    WHITE_KING_FILE = 1
    WHITE_KING_RANK = 2
    WHITE_ROOK_FILE = 3
    WHITE_ROOK_RANK = 4
    BLACK_KING_FILE = 5
    BLACK_KING_RANK = 6
    CLASS = 7

# attributes are in order by the Enum
chess_data = [
    ["1", "d", "1", "f", "3", "e", "4", "draw"],
    ["2", "a", "1", "f", "3", "g", "3", "draw"],
    ["3", "c", "2", "d", "6", "a", "1", "one"],
    ["4", "d", "2", "e", "8", "a", "1", "four"],
    ["5", "c", "3", "e", "8", "c", "1", "two"],
    ["6", "c", "3", "d", "4", "e", "1", "eight"],
    ["7", "d", "3", "a", "8", "f", "3", "nine"],
    ["8", "d", "3", "e", "2", "b", "1", "four"],
    ["9", "d", "3", "b", "8", "b", "1", "three"],
]

best_chess_attribute_data = DtreeMethods.find_best_attribute(chess_data)
print("best attribute in chess domain to split on:", CHESS_COLUMNS(best_chess_attribute_data[0]).name, "\n")
print("chess domain attribute value entropies:")
for attribute_value_tuple in best_chess_attribute_data[1]:
    print(CHESS_COLUMNS(attribute_value_tuple[0]).name, attribute_value_tuple[1],
          best_chess_attribute_data[1][attribute_value_tuple])
print()
print("chess domain attribute entropies:")
for attribute in best_chess_attribute_data[2]:
    print(CHESS_COLUMNS(attribute).name, best_chess_attribute_data[2][attribute])
print()
print("chess domain attribute information gains:")
for attribute in best_chess_attribute_data[3]:
    print(CHESS_COLUMNS(attribute).name, best_chess_attribute_data[3][attribute])
print()



# test divide_set_by_attribute
list_of_subset = DtreeMethods.divide_set_by_attribute(1, chess_data)
for subset in list_of_subset: 
    print("subset by : " ,subset)



