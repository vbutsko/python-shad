import string


def get_text_lines_with_words():
    text_lines = []
    n = int(input())
    for i in range(n):
        text_lines.append(input().lower())

    text_clean_words = []
    translator = str.maketrans(string.punctuation.replace("'", ""), ' '* (len(string.punctuation) - 1))
    for line in text_lines:
        text_clean_words.append(set(line.translate(translator).split()))
    return text_clean_words


def get_lines_with_words():
    words_lines = []
    m = int(input())
    for i in range(m):
        words_lines.append(set(input().lower().split()))
    return words_lines


text_line_sets = get_text_lines_with_words()
word_sets = get_lines_with_words()

for word_set in word_sets:
    result = []
    index = 1
    for text_line in text_line_sets:
        if word_set.issubset(text_line):
            result.append(str(index))
        index = index + 1
    print (-1 if len(result) == 0 else " ".join(result))
