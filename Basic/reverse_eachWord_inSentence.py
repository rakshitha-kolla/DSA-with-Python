def reverse(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
print(reverse("hello world good morning"))