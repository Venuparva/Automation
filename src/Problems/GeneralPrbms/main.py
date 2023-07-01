# This is a sample Python script.
from typing import List


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(paths: List[List[str]]):
    # Use a breakpoint in the code line below to debug your script.
    # outgoing_city = {}
    # for path in paths:
    #     city_first, city_second = path
    #     outgoing_city[city_first] = outgoing_city.get(city_first,0) + 1
    #     outgoing_city[city_second] = outgoing_city.get(city_second,0)
    #     print(outgoing_city)
    # #return filter(lambda x: outgoing_city.get(x) == 0)
    # for city in outgoing_city:
    #     if outgoing_city[city] == 0:
    #         print("DEST CITY:%s"%(city))
    #         return city
    A, B = map(set, zip(*paths))
    return (B-A).pop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputList = [['B', 'C'], ['D', 'B'], ['C', 'A']]
    result = print_hi(inputList)
    print("result:%s"%(result))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
