lookup = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
list = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def checkIndexForNumber(i, line):
    for item in list:
        try:
            index = line.index(item, i)
            if index == i:
                return lookup[item]
        except:
            continue
    
f = open("day-1-input.txt", "r")

total = 0
for line in f.readlines():
    numbersOnly = ''
    for i, letter in enumerate(line.strip()):
        addString = checkIndexForNumber(i, line)
        if addString:
            numbersOnly += addString
        elif letter.isdigit():
            numbersOnly += letter
    print(line, numbersOnly)
    print()
    numbersOnly = numbersOnly[0] + numbersOnly[-1]
    total += int(numbersOnly)
        

print(total)