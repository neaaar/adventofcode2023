import sys
import os
import re

def part1():
    sum = 0

    with open(os.path.join(sys.path[0], 'day2.txt'), 'r') as file:
        all_lines = file.read().splitlines()

        for line in all_lines:
            data_set = line.split(":")
            id = int(data_set[0].split(" ")[-1])
            line = line[line.find(":") + 1 : len(line)]

            red = 0
            green = 0
            blue = 0

            data_set = line.split(";")
            for data in data_set:
                words = data.split(",")

                for word in words:
                    if word.find("red") != -1:
                        if int(word.split(" ")[1]) > red:
                            red = int(word.split(" ")[1])
                    if word.find("green") != -1:
                        if int(word.split(" ")[1]) > green:
                            green = int(word.split(" ")[1])  
                    if word.find("blue") != -1:
                        if int(word.split(" ")[1]) > blue:
                            blue = int(word.split(" ")[1])    

            
            if(red <= 12 and green <= 13 and blue <= 14):
                sum += id
    
    print(sum)

def part2():
    sum = 0

    with open(os.path.join(sys.path[0], 'day2.txt'), 'r') as file:
        all_lines = file.read().splitlines()

        for line in all_lines:
            data_set = line.split(":")
            id = int(data_set[0].split(" ")[-1])
            line = line[line.find(":") + 1 : len(line)]

            red = 0
            green = 0
            blue = 0

            data_set = line.split(";")
            for data in data_set:
                words = data.split(",")

                for word in words:
                    if word.find("red") != -1:
                        if int(word.split(" ")[1]) > red:
                            red = int(word.split(" ")[1])
                    if word.find("green") != -1:
                        if int(word.split(" ")[1]) > green:
                            green = int(word.split(" ")[1])  
                    if word.find("blue") != -1:
                        if int(word.split(" ")[1]) > blue:
                            blue = int(word.split(" ")[1])    
            sum += red*green*blue
    
    print(sum)
    

if __name__ == "__main__":
    part1()
    part2()