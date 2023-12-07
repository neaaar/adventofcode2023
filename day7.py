import sys
import os

order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
order2 = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}

def part1():
    with open(os.path.join(sys.path[0], 'day7.txt'), 'r') as file:
        data = file.read().splitlines()

        five_of_a_kind = []
        four_of_a_kind = []
        full_house = []
        three_of_a_kind = []
        two_pair = []
        one_pair = []
        high_card = []

        for line in data:
            counters = [0, 0, 0, 0, 0]
            for i in range(len(line.split(" ")[0])):
                if(line[i] == line[0]):
                    counters[0] += 1
                if(line[i] == line[1]):
                    counters[1] += 1
                if(line[i] == line[2]):
                    counters[2] += 1
                if(line[i] == line[3]):
                    counters[3] += 1
                if(line[i] == line[4]):
                    counters[4] += 1

            if(counters.count(5) == 5):
                five_of_a_kind.append(line)
            elif(counters.count(4) == 4):
                four_of_a_kind.append(line)
            elif(counters.count(3) == 3 and counters.count(2) == 2):
                full_house.append(line)
            elif(counters.count(3) == 3):
                three_of_a_kind.append(line)
            elif(counters.count(2) == 4):
                two_pair.append(line)
            elif(counters.count(2) == 2):
                one_pair.append(line)
            elif(counters.count(1) == 5):
                high_card.append(line)

        five_of_a_kind.sort(key=lambda val : order[val[0]])
        five_of_a_kind.reverse()
        four_of_a_kind.sort(key=lambda val : order[val[0]])
        four_of_a_kind.reverse()
        full_house.sort(key=lambda val : order[val[0]])
        full_house.reverse()
        three_of_a_kind.sort(key=lambda val : order[val[0]])
        three_of_a_kind.reverse()
        two_pair.sort(key=lambda val : order[val[0]])
        two_pair.reverse()
        one_pair.sort(key=lambda val : order[val[0]])
        one_pair.reverse()
        high_card.sort(key=lambda val : order[val[0]])
        high_card.reverse()

        ordered_data = []
        ordered_data.append(five_of_a_kind)
        ordered_data.append(four_of_a_kind)
        ordered_data.append(full_house)
        ordered_data.append(three_of_a_kind)
        ordered_data.append(two_pair)
        ordered_data.append(one_pair)
        ordered_data.append(high_card)

        ordered_data = [_ for _ in ordered_data if _]

        sum = 0
        processed_data = 1
        ordered_data.reverse()
        for i in range(len(ordered_data)):
            for j in range(len(ordered_data[i])):
                sum += int(ordered_data[i][j].split(" ")[1]) * processed_data
                processed_data += 1
        print(sum)

def part2():
    with open(os.path.join(sys.path[0], 'day7.txt'), 'r') as file:
        data = file.read().splitlines()

        five_of_a_kind = []
        four_of_a_kind = []
        full_house = []
        three_of_a_kind = []
        two_pair = []
        one_pair = []
        high_card = []

        for line in data:
            counters = [0, 0, 0, 0, 0]
            for i in range(len(line.split(" ")[0])):
                if(line[i] == 'J'):
                    continue
                if(line[i] == line[0]):
                    counters[0] += 1
                if(line[i] == line[1]):
                    counters[1] += 1
                if(line[i] == line[2]):
                    counters[2] += 1
                if(line[i] == line[3]):
                    counters[3] += 1
                if(line[i] == line[4]):
                    counters[4] += 1
            for count in counters:
                count +=  line.count('J')
            
            if(counters.count(5) == 5):
                five_of_a_kind.append(line)
            elif(counters.count(4) == 4):
                four_of_a_kind.append(line)
            elif(counters.count(3) == 3 and counters.count(2) == 2):
                full_house.append(line)
            elif(counters.count(3) == 3):
                three_of_a_kind.append(line)
            elif(counters.count(2) == 4):
                two_pair.append(line)
            elif(counters.count(2) == 2):
                one_pair.append(line)
            elif(counters.count(1) == 5):
                high_card.append(line)

        five_of_a_kind.sort(key=lambda val : order2[val[0]])
        five_of_a_kind.reverse()
        four_of_a_kind.sort(key=lambda val : order2[val[0]])
        four_of_a_kind.reverse()
        full_house.sort(key=lambda val : order2[val[0]])
        full_house.reverse()
        three_of_a_kind.sort(key=lambda val : order2[val[0]])
        three_of_a_kind.reverse()
        two_pair.sort(key=lambda val : order2[val[0]])
        two_pair.reverse()
        one_pair.sort(key=lambda val : order2[val[0]])
        one_pair.reverse()
        high_card.sort(key=lambda val : order2[val[0]])
        high_card.reverse()

        ordered_data = []
        ordered_data.append(five_of_a_kind)
        ordered_data.append(four_of_a_kind)
        ordered_data.append(full_house)
        ordered_data.append(three_of_a_kind)
        ordered_data.append(two_pair)
        ordered_data.append(one_pair)
        ordered_data.append(high_card)

        ordered_data = [_ for _ in ordered_data if _]

        sum = 0
        processed_data = 1
        ordered_data.reverse()
        for i in range(len(ordered_data)):
            for j in range(len(ordered_data[i])):
                sum += int(ordered_data[i][j].split(" ")[1]) * processed_data
                processed_data += 1
        print(sum)

if __name__ == '__main__':
    part1()
    part2()