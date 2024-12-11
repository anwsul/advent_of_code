with open('./1.txt', 'r') as input:
    left = []
    right = []
    for line in input:
        pair = line.split()
        left.append(int(pair[0]))
        right.append(int(pair[1]))

left = sorted(left)
right = sorted(right)

def calculate_distance():
    distance = 0
    for l, r in zip(left, right):
        distance += abs(l - r)

    print(distance)

def find_similarity_score():
    score = 0
    for l in left:
        score += l * right.count(l)
    
    print(score)
        

calculate_distance()
find_similarity_score()