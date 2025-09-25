from collections import Counter


s = 'abracadabra'
count = {}
for letter in s:
    count[letter] = count.get(letter, 0) + 1
print(count)


sad = 'zaratustra'
print(f"zaratustra: {Counter(sad)}")



count_from_str = Counter('gallahad')  # создание Counter из строки
print(f"gallahad: {count_from_str}")


words = ['Donald', 'Mickey', 'Donald', 'Mickey', 'Mickey']
names = Counter(words)
print(names)

count_from_dict = Counter({'red': 4, 'blue': 2})  # создание Counter из словаря
print(count_from_dict)


def set_dict():
    players = {
    'Steven Brock': 800, 'Jennifer Murphy': 1600, 'Steven Brock': 1900,
    'Julie Sherman': 2000, 'Shannon Day': 2000, 'Lisa Singh': 1600,
    'Mark Burns': 1900, 'Christian Woodward': 1500, 'Kenneth Burke': 1200,
    'Kimberly Miller': 2100, 'Mrs. Amy Morton': 2200}
    #sort_players = Counter({key: value for key, value in players.items() if value > 900})
    sort_players = Counter({key: value for key, value in players.items() if key == 'Steven Brock'})
    print(sort_players)


def add_counters():
    counter1 = Counter({'a': 2, 'b': 3, 'c': 1})
    counter2 = Counter({'a': 1, 'b': 2, 'd': 4})
    result = counter1 + counter2
    print(result)


def minus_counters():
    c1 = Counter(a=3, b=1)
    c2 = Counter(a=1, b=2)
    c3 = c1 - c2
    print(c3)


def cross_counters():
    counter1 = Counter({'a': 2, 'b': 3, 'c': 1})
    counter2 = Counter({'a': 1, 'b': 2, 'd': 4})
    result = counter1 & counter2
    print(result)


def unite_counters():
    counter1 = Counter({'a': 2, 'b': 3, 'c': 1})
    counter2 = Counter({'a': 1, 'b': 2, 'd': 4})
    result = counter1 | counter2
    print(result)


print("\n")
unite_counters()

sales_1 = {'John': 10, 'Mary': 5, 'Bob': 3, 'Alice': 7}
sales_2 = {'John': 8, 'Mary': 4, 'Bob': 2, 'Alice': 6}
sales_3 = {'John': 6, 'Mary': 3, 'Bob': 1, 'Alice': 6}
def calculate_sales(*sales_dicts) -> Counter:
    result = Counter()
    for sale in sales_dicts:
        print(sale)
        result = result + Counter(sale)

    print(result)




statistics = {
    2010: {'Cristiano Ronaldo': 45, 'David Villa': 38, 'Diego Forlán': 35},
    2011: {'Cristiano Ronaldo': 60, 'David Villa': 73, 'Diego Forlán': 39},
    2012: {'Cristiano Ronaldo': 63, 'David Villa': 29, 'Diego Forlán': 16}
}
def count_goals(stats: dict) -> Counter:
    result = Counter()
    for key, val in stats.items():
        print(val)
        result = result + Counter(val)

    print(result)


def compare_lists(lst1: list, lst2: list) -> bool:
    mark = bool
    print(lst1, lst2)
    ls1 = sorted(lst1)
    ls2 = sorted(lst2)
    print(ls1, ls2)
    if len(ls1) == len(ls2):
        print("yes len")
        for i in range(0,len(ls1)):
            print(i)
            if ls1[i] == ls2[i]:
                print("while letters are good")
                continue
            else:
                print("fuck!")
                mark = False
                break
    else:
        print("no len")
        mark = False

    if mark: return True
    else: return False


sd = compare_lists([1, 2, 3, 4], [5, 3, 2, 1])
print(f"sd: {sd}")



def find_three_most_common(lst: list) -> list:
    ex_list = []
    c = Counter(lst)
    print(c.most_common(3))
    if len(c.most_common(3)) == 3:
        for i in c.most_common(3):
            print(i[0])
            ex_list.append(i[0])
        ex_list = sorted(ex_list)

    elif len(c.most_common(3)) == 2:
        ex_list.append(None)
        for i in c.most_common(3):
            print(i[0])
            ex_list.append(i[0])

    elif len(c.most_common(3)) == 1:
        ex_list.append(None)
        ex_list.append(None)
        for i in c.most_common(3):
            print(i[0])
            ex_list.append(i[0])

    else:
        ex_list = [None,None,None]

    print(ex_list)




find_three_most_common([1, 1, 2, 2, 2])

print([2,3,4] == [2,3,4])


def find_most_common_element(lst: list[int]):
    c = Counter(lst)
    d = c.most_common(1)
    print(d)
    print(d[0][0])
    #return d[1]


find_most_common_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4])


