
def swapcase_decorator(func):
    def wrapper(file_path):
        gen = func(file_path)
        while StopIteration:
            res = next(gen)
            yield res.swapcase()

    return wrapper



@swapcase_decorator
def duplicate_words_gen(file_path):
    duplicate_words = []
    with open(file_path) as f:
        data = f.read()
    words = data.split()
    for word in words:
        for chr in word:
            if word.count(chr) == 2:
                if word not in duplicate_words:
                    duplicate_words.append(word)
                    yield word

x = duplicate_words_gen('p3.txt')
while StopIteration:
    print(next(x))



