from DtreeMethods import DtreeMethods
from enum import Enum


class PIE_COLUMNS(Enum):
    CRUST_SIZE = 0
    SHAPE = 1
    FILLING_SIZE = 2
    CLASS = 3

# data must be in order from crust size, shape, filling size and class, according to the Enum
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
    WHITE_KING_FILE = 0
    WHITE_KING_RANK = 1
    WHITE_ROOK_FILE = 2
    WHITE_ROOK_RANK = 3
    BLACK_KING_FILE = 4
    BLACK_KING_RANK = 5
    CLASS = 6

chess_data = [
    ["d", "1", "f", "3", "e", "4", "draw"],
    ["a", "1", "f", "3", "g", "3", "draw"],
    ["c", "2", "d", "6", "a", "1", "one"],
    ["d", "2", "e", "8", "a", "1", "four"],
    ["c", "3", "e", "8", "c", "1", "two"],
    ["c", "3", "d", "4", "e", "1", "eight"],
    ["d", "3", "a", "8", "f", "3", "nine"],
    ["d", "3", "e", "2", "b", "1", "four"],
    ["d", "3", "b", "8", "b", "1", "three"],
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
