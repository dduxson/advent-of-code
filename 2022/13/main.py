import functools

def getPackets():
    packets = []
    with open("./2022/13/input.txt", "r") as file:
        for line in file.read().splitlines():
            if line:
                packets.append(eval(line))
    return packets

def compareInts(left_val, right_val):
    if left_val < right_val:
        return -1
    if left_val > right_val:
        return 1
    return 0

def compareLists(left_val, right_val):
    for i in range(min(len(left_val), len(right_val))):
        if isinstance(left_val[i], int) and isinstance(right_val[i], int):
            result = compareInts(left_val[i], right_val[i])
        else:
            left_list = left_val[i]
            right_list = right_val[i]
            if not isinstance(left_list, list):
                left_list = [left_list]
            if not isinstance(right_list, list):
                right_list = [right_list]
            result = compareLists(left_list, right_list)
        
        if result != 0:
            return result
    
    return compareInts(len(left_val), len(right_val))

def inOrderPacketPairs(packets):
    in_order_indexes = []
    for packet_index in range(0, len(packets), 2):
        if compareLists(packets[packet_index], packets[packet_index+1]) == -1:
            in_order_indexes.append((packet_index//2) +1)
    
    return in_order_indexes

def getDecoderKey(packets):
    result = 1
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=functools.cmp_to_key(compareLists))

    for i in range(len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            result *= i+1

    return result

def main():
    packets = getPackets()
    print(sum(inOrderPacketPairs(packets)))
    print(getDecoderKey(packets))

if __name__ == "__main__":
    main()