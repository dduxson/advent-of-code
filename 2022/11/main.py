from queue import Queue

class Item:
    #Mod worry with max_worry otherwise numbers get way too large.
    #Max worry should be a product of the test_dividor each monkey has.
    #Works as we only need to know whether worry is divisible by these test dividors.
    max_worry = 1

    def __init__(self, worry_level):
        self.__worry_level = worry_level

    def getWorryLevel(self):
        return self.__worry_level
    def setWorryLevel(self, value):
        self.__worry_level = value % Item.max_worry

class Monkey:
    def __init__(self, items, look_expression, test_dividor, true_monkey_index, false_monkey_index):
        self.__items = items
        self.__look_expression = look_expression
        self.__divisible_by = test_dividor
        self.__true_monkey_index = true_monkey_index
        self.__false_monkey_index = false_monkey_index
        self.__inspected_items_count = 0

    def addItem(self, item):
        self.__items.put(item)

    def transferItems(self, monkeys, player_worry_divisor):
        while not self.__items.empty():
            item = self.__items.get()
            item.setWorryLevel(eval(self.__look_expression) // player_worry_divisor)
            self.__inspected_items_count += 1
            if(item.getWorryLevel() % self.__divisible_by == 0):
                monkeys[self.__true_monkey_index].addItem(item)
            else:
                monkeys[self.__false_monkey_index].addItem(item)
    
    def getInspectedItemCount(self):
        return self.__inspected_items_count

def readMonkeysFromFile():
    monkeys = []
    with open("./2022/11/input.txt", "r") as file: 
        while True:
            line = file.readline()
            if not line:
                break
            if not line.startswith("Monkey"):
                continue
            
            monkey_items = Queue()
            item_worry_levels = file.readline().split("  Starting items: ",1)[1].split(", ")
            for worry_level in item_worry_levels:
                monkey_items.put(Item(int(worry_level)))
            look_expression = file.readline().split("  Operation: new = ",1)[1].replace("old", "item.getWorryLevel()")
            test_dividor = int(file.readline().split("  Test: divisible by ",1)[1])
            true_monkey_index = int(file.readline().split("    If true: throw to monkey ",1)[1])
            false_monkey_index = int(file.readline().split("    If false: throw to monkey ",1)[1])

            monkeys.append(Monkey(
                monkey_items, look_expression, \
                test_dividor, true_monkey_index, false_monkey_index \
            ))
            Item.max_worry *= test_dividor
    return monkeys

def playRounds(num, monkeys, player_worry_divisor):
    for i in range(num):
        for monkey in monkeys:
            monkey.transferItems(monkeys, player_worry_divisor)

def findMonkeyBusiness(monkeys):
    monkeys.sort(key=lambda x:x.getInspectedItemCount())
    return monkeys[-1].getInspectedItemCount() * monkeys[-2].getInspectedItemCount()

def main():
    monkeys = readMonkeysFromFile()
    playRounds(20, monkeys, 3)
    print(findMonkeyBusiness(monkeys))
    
    monkeys = readMonkeysFromFile()
    playRounds(10000, monkeys, 1)
    print(findMonkeyBusiness(monkeys))

if __name__ == "__main__":
    main()

