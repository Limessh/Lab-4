from itertools import combinations

class Item:
    def __init__(self, name, symbol, size, points):
        self.name = name
        self.symbol = symbol
        self.size = size
        self.points = points

items =[
    Item ("Винтовка", "r", 3, 25),
    Item ("Пистолет", "p", 2, 15),
    Item ("Боекомплект", "a", 2, 15),
    Item ("Аптечка", "m", 2, 20),
    Item ("Ингалятор", "i", 1, 5),
    Item ("Нож", "k", 1, 15),
    Item ("Топор", "x", 3, 20),
    Item ("Оберег", "t", 1, 25),
    Item ("Фляжка", "f", 1, 15),
    Item ("Антидот", "d", 1, 10),
    Item ("Еда", "s", 2, 20),
    Item ("Арбалет", "c", 2, 20)
    ]

start_points=10
bag_size=9
grid_size = 3
max_points=sum(item.points for item in items)

# bag_size= 7 # для 7 ячеек

def combination (items, max_size, individual_points):
    final_combination = []
    for i in range(1, len(items) + 1):
        for combination in combinations(items, i):
            final_size = sum(item.size for item in combination)
            combination_points = sum(item.points for item in combination)
            final_points = (max_points-combination_points) + individual_points
            if final_size<=max_size and final_points>0:
                final_combination.append(combination)
    return final_combination

combos = combination(items,bag_size, start_points)
# combos1 = combination(items,bag_size, start_points) # для 7 ячеек

def print_inventory (combos):
    for combo in combos:
        print("Комбинация:")
        combination = []
        for item in combo:
            size = item.size
            symbol = item.symbol
            for i in range (size):
                combination.append ([symbol])
        if len(combination)!= bag_size:
            while len(combination)!= bag_size:
                combination.append ([' '])
        # print (combination) # для 7 ячеек
        for j in range (0,bag_size,grid_size):
            print (combination[j],combination[j+1],combination[j+2])
            
print_inventory(combos)
# print_inventory(combos1) # для 7 ячеек