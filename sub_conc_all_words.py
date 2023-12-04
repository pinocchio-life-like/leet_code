def findSubstring(s, words):
    from collections import defaultdict

    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    num_words = len(words)
    word_len = len(words[0])
    indices = []

    for i in range(len(s) - num_words * word_len + 1):
        seen = defaultdict(int)
        for j in range(num_words):
            start = i + j * word_len
            word = s[start:start + word_len]
            if word not in word_count:
                break
            seen[word] += 1
            if seen[word] > word_count[word]:
                break
            if j + 1 == num_words:
                indices.append(i)

    return indices