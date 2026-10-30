def count_vowels(s, index=0):
    if index == len(s):
        return 0

    count = 1 if s[index].lower() in "aeiou" else 0

    return count + count_vowels(s, index + 1)


s = input()
print(count_vowels(s))