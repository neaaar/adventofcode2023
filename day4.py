import sys
import os
import re

def part1():
    with open(os.path.join(sys.path[0], 'day4.txt'), 'r') as file:
        total_points = 0
        for line in file.read().splitlines():
            card_points = 0
            line = line[line.find(':') + 1 : ]
            
            winning_numbers = line[ : line.find('|') - 1].split(' ')
            player_numbers = line[line.find('|') + 1 : ].split(' ')

            for number in player_numbers:
                if number == '' or number == ' ':
                    continue
                if number in winning_numbers:
                    if card_points == 0:
                        card_points = 1
                    else:
                        card_points *= 2
            total_points += card_points

    print(total_points)

def part2():
    with open(os.path.join(sys.path[0], 'day4.txt'), 'r') as file:
        total_cards = 0
        card_copies = []
        card_copies = [1 for i in range(202)]
        i = 0
        for line in file.read().splitlines():
            card_points = 0
            line = line[line.find(':') + 1 : ]
            
            winning_numbers = line[ : line.find('|') - 1].split(' ')
            player_numbers = line[line.find('|') + 1 : ].split(' ')

            for number in player_numbers:
                if number == '' or number == ' ':
                    continue
                if number in winning_numbers:
                    card_points += 1
                
            for l in range(card_points + 1):
                if(l == 0):
                    continue
                if(i + l) < 202:
                    card_copies[i + l] += 1*card_copies[i]
            i += 1
        print(sum(card_copies))



if __name__ == '__main__':
    part1()
    part2()