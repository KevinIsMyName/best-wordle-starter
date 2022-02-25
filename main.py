"""See README.md"""
FILENAME = "wordle-allowed-guesses.txt"  # File to read in

# Initialize our data structs
occurences_a = {}
occurences_b = {}
occurences_c = {}
occurences_d = {}
occurences_e = {}
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
for char in list(ALPHABET):
    occurences_a[char] = 0
    occurences_b[char] = 0
    occurences_c[char] = 0
    occurences_d[char] = 0
    occurences_e[char] = 0

# Populate frequency for each char pos
with open(FILENAME, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        word = line.strip()
        chars = list(word)
        a, b, c, d, e = chars
        occurences_a[a] += 1
        occurences_b[b] += 1
        occurences_c[c] += 1
        occurences_d[d] += 1
        occurences_e[e] += 1

# Calculate word scores
scores = {}
with open(FILENAME, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        word = line.strip()
        chars = list(word)
        a, b, c, d, e = chars
        score = (
            occurences_a[a]
            + occurences_b[b]
            + occurences_c[c]
            + occurences_d[d]
            + occurences_e[e]
        )  # Word score is just sum of each character's frequencies
        scores[word] = score

# Print our possible words, ascending.
# https://stackoverflow.com/questions/11228812/print-a-dict-sorted-by-values
d = scores
for v in sorted(d.values()):
    for key in d:
        if d[key] == v:
            print(key, v)
            break
