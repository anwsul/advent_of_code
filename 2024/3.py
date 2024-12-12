# I just need to do a parser
import re

with open("./3.txt", 'r') as input:
    memory_section = input.read()


def find_sum_from_corrupted_memory(memory_section):
    valid_sections = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", memory_section)

    sum = 0
    for section in valid_sections:
        sum += int(section[0]) * int(section[1])
    
    print(sum)


def find_sum_from_corrupted_memory_with_conditions(memory_section):
    sum = 0
    end = False
    read_instructions = True

    while(not end):
        upto = len(memory_section) - 1

        if read_instructions:
            _dont = re.search(r"don't\(\)", memory_section)

            if _dont:
                upto = _dont.end()
            else:
                end = True

            segment = memory_section[:upto]
            instructions = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", segment)

            for section in instructions:
                sum += int(section[0]) * int(section[1])
            
            read_instructions = False
            memory_section = memory_section[upto:]

        else:
            _do = re.search(r"do\(\)", memory_section)

            if _do:
                upto = _do.end()
            else:
                end = True
            
            read_instructions = True
            memory_section = memory_section[upto:]
        
    print(sum)  


find_sum_from_corrupted_memory(memory_section)
find_sum_from_corrupted_memory_with_conditions(memory_section)