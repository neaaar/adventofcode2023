import os
import sys

def part1():
    with open(os.path.join(sys.path[0], 'day15.txt'),'r') as file:
        steps = file.read().strip().split(',')
    
    res = 0
    for step in steps:
        hash_value = 0
        for character in step:
            hash_value += ord(character)
            hash_value *= 17
            hash_value %= 256
        res += hash_value
    print(res)

def part2():
    with open(os.path.join(sys.path[0], 'day15.txt'),'r') as file:
        steps = file.read().strip().split(',')
    
    boxes = [[] for _ in range(256)]
    res = 0
    for step in steps:
        op = 0 if '-' in step else 1
        characters, num = step.replace('-', '=').split('=')

        label_hash = 0
        for character in characters:
                label_hash += ord(character)
                label_hash *= 17
                label_hash %= 256
        
        if op == 0:
            boxes[label_hash] = [(ch, n) for (ch, n) in boxes[label_hash] if ch != characters]
        else:
            replaced = False
            for items in range(len(boxes[label_hash])):
                if characters == boxes[label_hash][items][0]:
                    boxes[label_hash][items] = (characters, num)
                    replaced = True
            if not replaced:
                boxes[label_hash].append((characters, num))
            
    res +=  sum((i + 1) * (j + 1) * int(boxes[i][j][1]) for i in range(256) for j in range(len(boxes[i])))  
    print(res)
        

            

if __name__ == '__main__':
    part1()
    part2()