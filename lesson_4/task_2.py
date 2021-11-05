source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([v for i, v in enumerate(source) if i > 0 and v > source[i - 1]])

print([source[i] for i in range(1, len(source)) if source[i] > source[i - 1]])
