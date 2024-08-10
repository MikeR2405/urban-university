
def all_variants(text):
    length = len(text)
    for sub_len in range(1, length + 1):
        for i in range(length - sub_len + 1):
            subsequence = text[i:i + sub_len]
            yield subsequence

a = all_variants("abc")
for i in a:
    print(i)