# 仮想番号
num = {
    "A": 140,
    "K": 130,
    "Q": 120,
    "J": 110,
    "T": 100,
    "9": 90,
    "8": 80,
    "7": 70,
    "6": 60,
    "5": 50,
    "4": 40,
    "3": 30,
    "2": 20,
}
# S > H > D > C
suit = {
    "S": 4,
    "H": 3,
    "D": 2,
    "C": 1,
}

# print(type(num["A"]))

# a = 111
# print(a // 10)
# print(a % 10)

# d = {
#     "a": 1,
#     "B": 2,
# }
# print(d["key"][1])

hand = ["H2", "C3", "HA", "H5", "C4"]

suit_of_hand = [x[0] for x in hand]
print(suit_of_hand.count("H"))