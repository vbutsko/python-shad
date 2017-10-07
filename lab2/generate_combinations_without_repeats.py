from itertools import combinations


def generate_combinations_without_repeats( words ):
    for i in range(2, len(words) + 1, 2):
        for combination in combinations(words, i):
            print (' '.join(combination))


words = sorted(set(input().lower().split(' ')))


generate_combinations_without_repeats(words)